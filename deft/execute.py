import shutil
from pathlib import Path
from typing import Optional

from config import CONFIG
from deft.deft_container import DeFTContainer
from deft.metadata import read_map_name


def resolve_map_name(frames_dir: Path, map_name: Optional[str]) -> Optional[str]:
    """
    Determine which HD map the extracted module tests were recorded on.

    Args:
        frames_dir (Path): Directory containing the extracted frames.
        map_name (Optional[str]): Explicitly requested map, if any.

    Returns:
        Optional[str]: The map to configure, or None when it is unknown.
    """
    return map_name or read_map_name(frames_dir)


def run_execute(
    frames_dir: Path,
    outputs_dir: Path,
    map_name: Optional[str] = None,
    set_map: bool = True,
):
    """
    Execute extracted module tests inside the DeFT container.

    Args:
        frames_dir (Path): Directory containing the extracted frames.
        outputs_dir (Path): Directory to store the execution outputs.
        map_name (Optional[str]): HD map to configure, overriding the map
            detected during extraction.
        set_map (bool): Whether to configure Apollo's HD map at all.
    """
    ctn = DeFTContainer(str(Path(CONFIG.APOLLO_ROOT)), 'deft')

    if set_map:
        resolved_map = resolve_map_name(frames_dir, map_name)
        if resolved_map is None:
            print(
                'HD map is unknown for these module tests; keeping the map '
                f'currently configured in Apollo ({ctn.get_map() or "none"}). '
                'Re-run `deft extract` or pass --map to set it explicitly.'
            )
        else:
            ctn.set_map(resolved_map)
            print(f'Apollo HD map set to {resolved_map}')

    print('Starting DeFT container...')

    if not ctn.is_running():
        ctn.start()

    assert ctn.is_running()

    if outputs_dir.exists():
        shutil.rmtree(outputs_dir)

    print('Loading testdata into container...')
    ctn.load_testdata(frames_dir)

    print('Running DeFT tests...')
    ctn.deft_run_tests()

    print('Saving outputs...')
    ctn.save_testdata(outputs_dir)

    ctn.stop()
    ctn.remove()

    print(f'Outputs saved to {outputs_dir}')


def main(parser):
    parser.add_argument(
        '--frames-dir',
        default='out/testdata',
        help='Directory containing extracted frames',
    )

    parser.add_argument(
        '--outputs-dir',
        default='out/testdata_out',
        help='Directory to store execution outputs',
    )

    parser.add_argument(
        '--map',
        default=None,
        help='HD map to configure, overriding the one detected during extraction',
    )

    parser.add_argument(
        '--no-set-map',
        action='store_true',
        help="Do not configure Apollo's HD map before executing module tests",
    )

    def handler(args):
        frames_dir = Path(args.frames_dir)
        outputs_dir = Path(args.outputs_dir)

        if not frames_dir.exists():
            parser.error('Frames directory does not exist')

        run_execute(
            frames_dir,
            outputs_dir,
            map_name=args.map,
            set_map=not args.no_set_map,
        )

    parser.set_defaults(func=handler)
