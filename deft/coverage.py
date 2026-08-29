import shutil
from pathlib import Path
from typing import Optional

from config import CONFIG
from deft.deft_container import DeFTContainer
from deft.execute import resolve_map_name


def run_coverage(
    frames_dir: Path,
    report_dir: Path,
    map_name: Optional[str] = None,
    set_map: bool = True,
    keep_container: bool = False,
    show_container_output: bool = False,
):
    """
    Compute planning code coverage of extracted module tests.

    Args:
        frames_dir (Path): Directory containing the extracted frames.
        report_dir (Path): Directory to store the generated coverage report.
        map_name (Optional[str]): HD map to configure, overriding the map
            detected during extraction.
        set_map (bool): Whether to configure Apollo's HD map at all.
        keep_container (bool): Whether to leave the container running after the
            coverage run finishes, so that repeated runs reuse the same
            container instead of restarting it.
        show_container_output (bool): Whether to show the output of the
            coverage run happening inside the container.
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

    print('Loading testdata into container...')
    ctn.load_testdata(frames_dir)

    print('Computing planning coverage (this takes a while)...')
    ctn.deft_coverage(show_container_output=show_container_output)

    if report_dir.exists():
        shutil.rmtree(report_dir)

    print('Saving coverage report...')
    ctn.save_genhtml(report_dir)

    if keep_container:
        print('Keeping DeFT container running...')
    else:
        ctn.stop()
        ctn.remove()

    if not report_dir.exists():
        raise SystemExit(
            'Coverage report was not produced inside the container; '
            're-run with --show-container-output to see what went wrong.'
        )

    print(f'Coverage report saved to {report_dir / "index.html"}')


def main(parser):
    parser.add_argument(
        '--frames-dir',
        default='out/testdata',
        help='Directory containing extracted frames',
    )

    parser.add_argument(
        '--report-dir',
        default='out/coverage',
        help='Directory to store the generated coverage report',
    )

    parser.add_argument(
        '--map',
        default=None,
        help='HD map to configure, overriding the one detected during extraction',
    )

    parser.add_argument(
        '--no-set-map',
        action='store_true',
        help="Do not configure Apollo's HD map before computing coverage",
    )

    parser.add_argument(
        '--keep-container',
        action='store_true',
        help='Leave the DeFT container running after computing coverage '
        'instead of stopping and removing it',
    )

    parser.add_argument(
        '--show-container-output',
        action='store_true',
        help='Show the output of the coverage run inside the container',
    )

    def handler(args):
        frames_dir = Path(args.frames_dir)
        report_dir = Path(args.report_dir)

        if not frames_dir.exists():
            parser.error('Frames directory does not exist')

        run_coverage(
            frames_dir,
            report_dir,
            map_name=args.map,
            set_map=not args.no_set_map,
            keep_container=args.keep_container,
            show_container_output=args.show_container_output,
        )

    parser.set_defaults(func=handler)
