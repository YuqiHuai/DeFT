import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, OrderedDict

from cyber_record.record import Record

from apollo_oracle.utils.map_service import MapService
from apollo_oracle.utils.vehicle_param import VehicleParam

if sys.version_info >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata


@dataclass(slots=True)
class Violation:
    name: str
    triggered: bool
    features: Dict

    def asdict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        for k in ['name', 'triggered', 'features']:
            assert k in data, f'Key {k} not in {data}'

        assert isinstance(data['name'], str)
        assert isinstance(data['triggered'], bool)
        assert isinstance(data['features'], dict)

        return Violation(data['name'], data['triggered'], data['features'])


class OracleExtension(object):
    def __init__(
        self, map_service: MapService, vehicle_param: VehicleParam, args_dict: Dict
    ):
        self.map_service = map_service
        self.vehicle_param = vehicle_param
        self.args_dict = args_dict

    def get_interested_topics(self) -> List[str]:
        return []

    def on_message(self, topic: str, msg: Any, t: float) -> None:
        pass

    def get_violations(self) -> List[Violation]:
        return []

    @staticmethod
    def get_name() -> str:
        raise NotImplementedError

    @staticmethod
    def register_arguments(parser):
        pass


class OracleInterrupt(Exception):
    pass


class OracleExtensionManager:
    def __init__(self):
        self.available_extensions = list_plugins()

    def extend_cli_parser(self, parser):
        for p in self.available_extensions.values():
            p.register_arguments(parser)

    def get_active_extensions(
        self,
        all_oracle_active: bool,
        included_oracles: List[str],
        excluded_oracles: List[str],
    ):
        plugins = list_plugins()

        if all_oracle_active:
            return plugins.values()

        oracles = [x for x in plugins]

        if len(included_oracles) > 0 and len(excluded_oracles) > 0:
            oracles = [
                x
                for x in oracles
                if x in included_oracles and x not in excluded_oracles
            ]
        elif len(included_oracles) > 0:
            oracles = [x for x in oracles if x in included_oracles]
        elif len(excluded_oracles) > 0:
            oracles = [x for x in oracles if x not in excluded_oracles]

        return [plugins[x] for x in oracles]


def list_plugins(extension_point='apollo_oracle.extensions'):
    all_entry_points = importlib_metadata.entry_points()
    if hasattr(all_entry_points, 'select'):
        extensions = all_entry_points.select(group=extension_point)
    else:
        extensions = all_entry_points.get(extension_point, [])
    unordered_oracles = {
        entry_point.name: entry_point.load() for entry_point in extensions
    }

    plugin_names = list(unordered_oracles.keys())
    plugin_names.sort()
    return OrderedDict(
        [(plugin_name, unordered_oracles[plugin_name]) for plugin_name in plugin_names]
    )


def analyze_record(
    oracle_instances: List[OracleExtension],
    record_file: Path,
):
    record_file = Record(record_file)
    found_routing_request = False
    try:
        for topic, msg, t in record_file.read_messages():
            if topic == '/apollo/routing_request':
                found_routing_request = True
            if not found_routing_request:
                continue
            for oracle_instance in oracle_instances:
                if topic in oracle_instance.get_interested_topics():
                    oracle_instance.on_message(topic, msg, t)
    except OracleInterrupt:
        pass
    violations: List[Violation] = list()
    for oracle_instance in oracle_instances:
        violations.extend(oracle_instance.get_violations())

    return violations
