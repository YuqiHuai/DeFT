import shutil
from pathlib import Path
from typing import Optional

from deft.impl.deft_apollo import DeFTApollo
from deft.impl.deft_heuristic import DeFTHeuristic
from deft.impl.deft_log import DeFTLog
from deft.map_detect import MapDetectionError, describe, detect_map
from deft.metadata import write_metadata

IMPLEMENTATIONS = {
    'apollo': DeFTApollo,
    'heuristic': DeFTHeuristic,
    'log': DeFTLog,
}


def run_extract(
    record_path: Path,
    frames_dir: Path,
    map_name: Optional[str] = None,
    detect_map_enabled: bool = True,
    impl: str = 'apollo',
):
    """
    Extract module tests from a scenario record.

    Args:
        record_path (Path): Path to the scenario record file.
        frames_dir (Path): Directory to store the extracted frames.
        map_name (Optional[str]): HD map to record, skipping detection.
        detect_map_enabled (bool): Whether to detect the HD map from the record.
        impl (str): Which DeFT implementation reconstructs the frames. Records
            produced by an Apollo carrying the DeFT instrumentation expose the
            true input identifiers in ``msg.deft.*``; ``log`` reads them
            directly instead of inferring them.
    """
    detected_map = map_name

    if map_name is None and detect_map_enabled:
        print('Detecting HD map ...')
        try:
            result = detect_map(record_path)
            print(describe(result))
            detected_map = result.map_name
        except MapDetectionError as e:
            print(f'HD map detection failed: {e}')

    agent = IMPLEMENTATIONS[impl]()

    print(f'Extracting frames ({impl}) ...')
    frames = agent.extract_frames(str(record_path))

    if frames_dir.exists():
        shutil.rmtree(frames_dir)

    print('Writing frames to file...')
    agent.write_frames_to_file(frames, frames_dir)

    write_metadata(
        frames_dir,
        {
            'record': str(record_path),
            'map': detected_map,
            'impl': impl,
            'num_frames': len(frames),
        },
    )

    print(f'Frames saved to {frames_dir}')


def main(parser):
    parser.add_argument(
        'record',
        help='Path to scenario record file',
    )

    parser.add_argument(
        '--frames-dir',
        default='out/testdata',
        help='Directory to store extracted frames',
    )

    parser.add_argument(
        '--map',
        default=None,
        help='HD map used by the record (skips automatic detection)',
    )

    parser.add_argument(
        '--impl',
        default='apollo',
        choices=sorted(IMPLEMENTATIONS),
        help='Implementation used to reconstruct frames. Use "log" for records '
        'from an Apollo carrying the DeFT instrumentation, which stores the '
        'true frame time and input headers in msg.deft.*',
    )

    parser.add_argument(
        '--no-detect-map',
        action='store_true',
        help='Do not detect the HD map used by the record',
    )

    def handler(args):
        record = Path(args.record)
        frames_dir = Path(args.frames_dir)

        if not record.exists():
            parser.error('Scenario record file does not exist')

        run_extract(
            record,
            frames_dir,
            map_name=args.map,
            detect_map_enabled=not args.no_detect_map,
            impl=args.impl,
        )

    parser.set_defaults(func=handler)
