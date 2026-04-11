import shutil
from pathlib import Path

from deft.impl.deft_log import DeFTLog
from deft.impl.deft_heuristic import DeFTHeuristic


def run_extract(record_path: Path, frames_dir: Path):
    agent = DeFTLog()

    print('Extracting frames ...')
    frames = agent.extract_frames(str(record_path))

    if frames_dir.exists():
        shutil.rmtree(frames_dir)

    print('Writing frames to file...')
    agent.write_frames_to_file(frames, frames_dir)

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

    def handler(args):
        record = Path(args.record)
        frames_dir = Path(args.frames_dir)

        if not record.exists():
            parser.error('Scenario record file does not exist')

        run_extract(record, frames_dir)

    parser.set_defaults(func=handler)
