"""Automatic HD map detection for Apollo record files.

Apollo's planning module resolves the lane and road identifiers published on
``/apollo/routing_response`` against whichever HD map is configured through
``--map_dir``. Module tests extracted by DeFT are therefore only reproducible
when the container runs with the same map that produced the record, which so
far had to be selected by hand (``scripts/set_hd_map.sh``) before running
``deft execute``.

This module recovers that map from the record itself. The routing response is
compared against the topology graph (``routing_map.bin``) of every map under
``data/maps`` using four pieces of evidence:

* **lane coverage** - every lane id referenced by the route must exist in the
  map. This is a hard filter, but it is not sufficient on its own: the lane ids
  of ``borregas_ave`` are a strict subset of ``san_francisco``'s, and the three
  ``sunnyvale_*`` maps share thousands of ids.
* **road ids** - each routed lane must belong to the road id reported in the
  corresponding ``RoadSegment``.
* **lane lengths** - the routed ``end_s`` of a lane must fit within the lane
  length recorded in the map.
* **waypoint geometry** - the pose of a routing request waypoint must land on
  the map's lane geometry at the requested arc length ``s``.
* **map version** - ``RoutingResponse.map_version`` must match the map's
  ``hdmap_version``.

When the record also contains ``/apollo/hmi/status``, its ``current_map`` field
(the map Dreamview had loaded during the scenario) is used as a corroborating
hint, but only when the routing evidence agrees that the map is viable.
"""

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from cyber_record.record import Record
from google.protobuf import text_format

from apollo_modules.modules.routing.proto.routing_pb2 import RoutingResponse
from apollo_modules.modules.routing.proto.topo_graph_pb2 import Graph
from config import CONFIG
from deft.utils.apollo_topics import ApolloTopics

DEFAULT_MAPS_DIR = Path(CONFIG.PROJECT_ROOT, 'data', 'maps')

# Relative weights of the individual pieces of evidence. They sum up to 1.0 so
# that a perfect match scores exactly 1.0.
ROAD_WEIGHT = 0.4
LENGTH_WEIGHT = 0.3
GEOMETRY_WEIGHT = 0.2
VERSION_WEIGHT = 0.1

# A routed lane may end slightly beyond the length stored in the map because of
# floating point rounding in the routing module.
LENGTH_TOLERANCE = 0.01

# Two candidates whose scores differ by less than this are considered tied.
SCORE_EPSILON = 1e-6


class MapDetectionError(RuntimeError):
    """Raised when the HD map used by a record cannot be determined."""


@dataclass
class RoutedLane:
    """A lane referenced by the route, together with its road id."""

    lane_id: str
    start_s: float
    end_s: float
    road_id: str


@dataclass
class RoutedWaypoint:
    """A routing request waypoint whose pose can be checked geometrically."""

    lane_id: str
    s: float
    x: float
    y: float


@dataclass
class RoutingSignature:
    """The map-identifying information carried by a routing response."""

    lanes: List[RoutedLane] = field(default_factory=list)
    waypoints: List[RoutedWaypoint] = field(default_factory=list)
    map_version: str = ''
    hmi_map: str = ''


@dataclass
class MapFingerprint:
    """The map-side counterpart of a :class:`RoutingSignature`."""

    name: str
    version: str
    lane_lengths: Dict[str, float] = field(default_factory=dict)
    lane_roads: Dict[str, str] = field(default_factory=dict)
    # Central curve points, only kept for the lanes we actually check.
    lane_curves: Dict[str, List[Tuple[float, float]]] = field(default_factory=dict)


@dataclass
class MapMatch:
    """How well a single map explains a routing signature."""

    name: str
    score: float
    lane_coverage: float
    road_match: float
    length_match: float
    version_match: bool
    waypoint_error: Optional[float]

    @property
    def is_viable(self) -> bool:
        return self.lane_coverage >= 1.0


@dataclass
class DetectionResult:
    """Outcome of map detection for a single record."""

    map_name: Optional[str]
    matches: List[MapMatch]
    hmi_map: str = ''
    hmi_confirmed: bool = False
    ambiguous: bool = False

    @property
    def best(self) -> Optional[MapMatch]:
        for match in self.matches:
            if match.name == self.map_name:
                return match
        return None

    @property
    def score(self) -> float:
        best = self.best
        return best.score if best else 0.0

    @property
    def runner_up(self) -> Optional[MapMatch]:
        for match in self.matches:
            if match.name != self.map_name:
                return match
        return None


def normalize_map_name(display_name: str) -> str:
    """
    Convert a Dreamview map name into the directory name used on disk.

    Args:
        display_name (str): Map name as published by HMI, e.g. 'Sunnyvale Loop'.

    Returns:
        str: The corresponding directory name, e.g. 'sunnyvale_loop'.
    """
    return '_'.join(display_name.lower().split())


def extract_routing_signature(record_path: Path) -> RoutingSignature:
    """
    Read the map-identifying information out of a scenario record.

    Only the first routing response is needed; a route cannot span two maps.

    Args:
        record_path (Path): Path to the scenario record file.

    Returns:
        RoutingSignature: The extracted signature.

    Raises:
        MapDetectionError: If the record contains no routing response.
    """
    record = Record(str(record_path))

    response: Optional[RoutingResponse] = None
    for _, msg, _ in record.read_messages(ApolloTopics.ROUTING_RESPONSE):
        response = msg
        break

    if response is None:
        raise MapDetectionError(
            f'{record_path} contains no {ApolloTopics.ROUTING_RESPONSE} message, '
            'the HD map cannot be detected'
        )

    signature = RoutingSignature()

    for road in response.road:
        for passage in road.passage:
            for segment in passage.segment:
                signature.lanes.append(
                    RoutedLane(segment.id, segment.start_s, segment.end_s, road.id)
                )

    for waypoint in response.routing_request.waypoint:
        if not waypoint.HasField('pose'):
            continue
        if not (math.isfinite(waypoint.pose.x) and math.isfinite(waypoint.pose.y)):
            continue
        signature.waypoints.append(
            RoutedWaypoint(
                waypoint.id, waypoint.s, waypoint.pose.x, waypoint.pose.y
            )
        )

    if response.map_version:
        signature.map_version = response.map_version.decode('utf-8', 'replace')

    for _, msg, _ in record.read_messages(ApolloTopics.HMI_STATUS):
        if msg.current_map:
            signature.hmi_map = msg.current_map
        break

    if not signature.lanes:
        raise MapDetectionError(
            f'{record_path} contains an empty route, the HD map cannot be detected'
        )

    return signature


def _load_topo_graph(map_dir: Path) -> Optional[Graph]:
    """
    Load the routing topology graph of a map directory, if there is one.

    Args:
        map_dir (Path): Directory of a single HD map.

    Returns:
        Optional[Graph]: The parsed graph, or None when the map has no
        routing map (and can therefore not be matched against a route).
    """
    graph = Graph()

    binary_map = Path(map_dir, 'routing_map.bin')
    if binary_map.exists():
        with open(binary_map, 'rb') as fp:
            graph.ParseFromString(fp.read())
        return graph

    text_map = Path(map_dir, 'routing_map.txt')
    if text_map.exists():
        with open(text_map, 'r') as fp:
            text_format.Parse(fp.read(), graph)
        return graph

    return None


def build_fingerprint(
    map_dir: Path, curve_lane_ids: Sequence[str] = ()
) -> Optional[MapFingerprint]:
    """
    Summarize a map directory into the data needed to match a route.

    Lane geometry is expensive to keep around, so central curves are only
    retained for ``curve_lane_ids`` (the lanes referenced by routing request
    waypoints).

    Args:
        map_dir (Path): Directory of a single HD map.
        curve_lane_ids (Sequence[str]): Lane ids whose geometry is needed.

    Returns:
        Optional[MapFingerprint]: The fingerprint, or None if the directory is
        not a usable map.
    """
    graph = _load_topo_graph(map_dir)
    if graph is None:
        return None

    wanted_curves = set(curve_lane_ids)
    fingerprint = MapFingerprint(name=map_dir.name, version=graph.hdmap_version)

    for node in graph.node:
        fingerprint.lane_lengths[node.lane_id] = node.length
        fingerprint.lane_roads[node.lane_id] = node.road_id
        if node.lane_id in wanted_curves:
            fingerprint.lane_curves[node.lane_id] = [
                (point.x, point.y)
                for segment in node.central_curve.segment
                for point in segment.line_segment.point
            ]

    if not fingerprint.lane_lengths:
        return None

    return fingerprint


def load_fingerprints(
    maps_dir: Path = DEFAULT_MAPS_DIR, curve_lane_ids: Sequence[str] = ()
) -> List[MapFingerprint]:
    """
    Build fingerprints for every map available under a maps directory.

    Args:
        maps_dir (Path): Directory containing one sub-directory per HD map.
        curve_lane_ids (Sequence[str]): Lane ids whose geometry is needed.

    Returns:
        List[MapFingerprint]: One fingerprint per usable map.

    Raises:
        MapDetectionError: If the maps directory does not exist.
    """
    if not maps_dir.is_dir():
        raise MapDetectionError(f'Maps directory does not exist: {maps_dir}')

    fingerprints = []
    for map_dir in sorted(maps_dir.iterdir()):
        if not map_dir.is_dir():
            continue
        fingerprint = build_fingerprint(map_dir, curve_lane_ids)
        if fingerprint is not None:
            fingerprints.append(fingerprint)
    return fingerprints


def point_at_arc_length(
    points: Sequence[Tuple[float, float]], s: float
) -> Optional[Tuple[float, float]]:
    """
    Interpolate the point located ``s`` meters along a polyline.

    Args:
        points (Sequence[Tuple[float, float]]): The polyline vertices.
        s (float): Arc length measured from the first vertex.

    Returns:
        Optional[Tuple[float, float]]: The interpolated point, or None when the
        polyline is empty.
    """
    if not points:
        return None

    travelled = 0.0
    for start, end in zip(points, points[1:]):
        length = math.dist(start, end)
        if travelled + length >= s:
            ratio = (s - travelled) / length if length > 0 else 0.0
            return (
                start[0] + ratio * (end[0] - start[0]),
                start[1] + ratio * (end[1] - start[1]),
            )
        travelled += length
    return points[-1]


def score_map(signature: RoutingSignature, fingerprint: MapFingerprint) -> MapMatch:
    """
    Score how well a map explains a routing signature.

    Args:
        signature (RoutingSignature): Signature extracted from a record.
        fingerprint (MapFingerprint): Fingerprint of a candidate map.

    Returns:
        MapMatch: The resulting score and its individual components.
    """
    total = len(signature.lanes)
    known = [
        lane for lane in signature.lanes if lane.lane_id in fingerprint.lane_lengths
    ]
    lane_coverage = len(known) / total if total else 0.0

    if known:
        road_match = sum(
            1
            for lane in known
            if fingerprint.lane_roads.get(lane.lane_id) == lane.road_id
        ) / len(known)
        length_match = sum(
            1
            for lane in known
            if lane.end_s
            <= fingerprint.lane_lengths[lane.lane_id] + LENGTH_TOLERANCE
        ) / len(known)
    else:
        road_match = 0.0
        length_match = 0.0

    distances = []
    for waypoint in signature.waypoints:
        curve = fingerprint.lane_curves.get(waypoint.lane_id)
        if not curve:
            continue
        projected = point_at_arc_length(curve, waypoint.s)
        if projected is None:
            continue
        distances.append(math.dist(projected, (waypoint.x, waypoint.y)))

    if distances:
        waypoint_error = sum(distances) / len(distances)
        # Maps that cannot be checked geometrically keep the neutral score of
        # 1.0, so this must stay in [0, 1] and decay with the error.
        geometry_score = 1.0 / (1.0 + waypoint_error)
    else:
        waypoint_error = None
        geometry_score = 1.0

    version_match = bool(
        signature.map_version and signature.map_version == fingerprint.version
    )

    score = (
        ROAD_WEIGHT * road_match
        + LENGTH_WEIGHT * length_match
        + GEOMETRY_WEIGHT * geometry_score
        + VERSION_WEIGHT * (1.0 if version_match else 0.0)
    )

    return MapMatch(
        name=fingerprint.name,
        score=score,
        lane_coverage=lane_coverage,
        road_match=road_match,
        length_match=length_match,
        version_match=version_match,
        waypoint_error=waypoint_error,
    )


def detect_map_from_signature(
    signature: RoutingSignature, maps_dir: Path = DEFAULT_MAPS_DIR
) -> DetectionResult:
    """
    Determine which map a routing signature was produced on.

    Args:
        signature (RoutingSignature): Signature extracted from a record.
        maps_dir (Path): Directory containing the known HD maps.

    Returns:
        DetectionResult: The detected map along with all ranked candidates.
    """
    curve_lane_ids = [waypoint.lane_id for waypoint in signature.waypoints]
    fingerprints = load_fingerprints(maps_dir, curve_lane_ids)

    matches = [score_map(signature, fingerprint) for fingerprint in fingerprints]
    viable = sorted(
        (match for match in matches if match.is_viable),
        key=lambda match: match.score,
        reverse=True,
    )

    result = DetectionResult(map_name=None, matches=viable, hmi_map=signature.hmi_map)

    if not viable:
        return result

    result.map_name = viable[0].name
    result.ambiguous = (
        len(viable) > 1 and viable[0].score - viable[1].score < SCORE_EPSILON
    )

    # The HMI status reports the map Dreamview had loaded while the scenario
    # ran. Trust it only when the routing evidence agrees that the map is a
    # viable candidate.
    if signature.hmi_map:
        hinted = normalize_map_name(signature.hmi_map)
        for match in viable:
            if match.name == hinted:
                result.map_name = hinted
                result.hmi_confirmed = True
                result.ambiguous = False
                break

    return result


def detect_map(
    record_path: Path, maps_dir: Path = DEFAULT_MAPS_DIR
) -> DetectionResult:
    """
    Determine which HD map a scenario record was produced on.

    Args:
        record_path (Path): Path to the scenario record file.
        maps_dir (Path): Directory containing the known HD maps.

    Returns:
        DetectionResult: The detected map along with all ranked candidates.

    Raises:
        MapDetectionError: If the record carries no usable routing response.
    """
    signature = extract_routing_signature(Path(record_path))
    return detect_map_from_signature(signature, maps_dir)


def describe(result: DetectionResult) -> str:
    """
    Render a detection result as a human readable report.

    Args:
        result (DetectionResult): The result to describe.

    Returns:
        str: A multi-line report listing every viable candidate.
    """
    lines = []
    if result.map_name is None:
        lines.append('No map under data/maps contains every lane of the route.')
    else:
        source = 'routing response'
        if result.hmi_confirmed:
            source = 'routing response, confirmed by /apollo/hmi/status'
        lines.append(
            f'Detected map: {result.map_name} '
            f'(score {result.score:.3f}, via {source})'
        )
        if result.ambiguous:
            lines.append(
                'Warning: the route matches several maps equally well; '
                'pass --map to choose explicitly.'
            )
        if result.hmi_map and not result.hmi_confirmed:
            lines.append(
                f"Warning: /apollo/hmi/status reports '{result.hmi_map}', which is "
                'not among the maps matching the route.'
            )

    for match in result.matches:
        marker = '*' if match.name == result.map_name else ' '
        error = (
            'n/a' if match.waypoint_error is None else f'{match.waypoint_error:.3f}m'
        )
        lines.append(
            f'  {marker} {match.name:<28} score={match.score:.3f} '
            f'lanes={match.lane_coverage:.0%} roads={match.road_match:.0%} '
            f'lengths={match.length_match:.0%} version={match.version_match} '
            f'waypoint_error={error}'
        )
    return '\n'.join(lines)
