from pathlib import Path

from deft.map_detect import (
    DEFAULT_MAPS_DIR,
    MapDetectionError,
    describe,
    detect_map,
)


def run_detect(record_path: Path, maps_dir: Path) -> bool:
    """
    Report which HD map a scenario record was produced on.

    Args:
        record_path (Path): Path to the scenario record file.
        maps_dir (Path): Directory containing the known HD maps.

    Returns:
        bool: True when a map was detected.
    """
    result = detect_map(record_path, maps_dir)
    print(describe(result))
    return result.map_name is not None


def main(parser):
    parser.add_argument(
        'record',
        help='Path to scenario record file',
    )

    parser.add_argument(
        '--maps-dir',
        default=str(DEFAULT_MAPS_DIR),
        help='Directory containing the known HD maps',
    )

    def handler(args):
        record = Path(args.record)
        maps_dir = Path(args.maps_dir)

        if not record.exists():
            parser.error('Scenario record file does not exist')

        try:
            detected = run_detect(record, maps_dir)
        except MapDetectionError as e:
            parser.error(str(e))

        if not detected:
            raise SystemExit(1)

    parser.set_defaults(func=handler)
