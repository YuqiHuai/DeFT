import shutil
from pathlib import Path
from typing import Dict, List, Optional

from config import CONFIG
from deft.deft_container import DeFTContainer
from deft.execute import resolve_map_name
from deft.extract import IMPLEMENTATIONS, run_extract
from deft.planning_flags import parse_flag, planning_flags


def find_corrupt_sources(tracefile: Path, source_root: Path) -> List[str]:
    """
    Find sources whose coverage cannot belong to them.

    gcov writes its counters when the instrumented test exits, so a run that
    was interrupted leaves half-written data behind, which parses into
    coverage attributed to lines past the end of the file it claims to be.
    Such a tracefile is not merely incomplete: unioned with others it inflates
    the line total of every technique it is part of, so it has to be caught
    rather than merged.

    Args:
        tracefile (Path): The LCOV tracefile to check.
        source_root (Path): Directory the tracefile's paths are relative to.

    Returns:
        List[str]: One description per source whose records overrun it.
    """
    problems = []
    current = None
    highest = 0

    def check():
        if current is None:
            return
        source = source_root / current
        if not source.is_file():
            return
        with open(source, 'rb') as fp:
            length = sum(1 for _ in fp)
        if highest > length:
            problems.append(f'{current}: line {highest} of a {length}-line file')

    with open(tracefile) as fp:
        for line in fp:
            if line.startswith('SF:'):
                check()
                current = line[3:].strip()
                highest = 0
            elif line.startswith('DA:'):
                number = int(line[3:].split(',', 1)[0])
                highest = max(highest, number)
    check()

    return problems


def run_coverage(
    frames_dir: Path,
    report_dir: Path,
    map_name: Optional[str] = None,
    set_map: bool = True,
    keep_container: bool = False,
    show_container_output: bool = False,
    flags: Optional[Dict[str, str]] = None,
    lcov_path: Optional[Path] = None,
    gcda_path: Optional[Path] = None,
    gcno_path: Optional[Path] = None,
    save_report: bool = True,
    apollo_root: Optional[Path] = None,
    user: str = 'deft',
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
        flags (Optional[Dict[str, str]]): Planning gflags to write into
            planning.conf for this run, restored afterwards. The module tests
            read planning.conf at startup, so a scenario executed under
            non-default flags must have them applied here to exercise the same
            code paths.
        lcov_path (Optional[Path]): Where to write the raw LCOV tracefile,
            defaulting to ``coverage.dat`` inside the report directory. The
            tracefile, unlike the HTML rendering of it, can be unioned and
            differenced across runs, so it is what makes coverage from separate
            records comparable.
        gcda_path (Optional[Path]): Where to save this run's raw gcov
            counters, as a ``.tar.gz``. Skipped when None. An LCOV tracefile
            keeps only whether an entity was hit, so questions the tracefile
            cannot answer -- decision-only branch coverage, execution counts --
            otherwise require covering every record again, which is days of
            machine time. Keeping the counters makes that a re-read instead.
        gcno_path (Optional[Path]): Where to save the gcov notes that decode
            those counters. Identical for every record covered against one
            build, so a batch should ask for this once, not per record.
        save_report (bool): Whether to copy the HTML rendering out of the
            container. Batch runs over many records only need the tracefiles,
            and copying a report per record costs far more than producing one.
        apollo_root (Optional[Path]): The Apollo checkout to run against,
            defaulting to the one installed beside this project. Workers run
            concurrently only if each has its own checkout: /apollo is a bind
            mount, and a run rewrites planning.conf, the scenario textprotos
            and the HD-map flagfile inside it, besides holding the Bazel
            output base the test writes its coverage data to.
        user (str): Container user, which also names the container
            (apollo_dev_<user>) and its in-container work directory. Give
            concurrent workers distinct names, zero-padded: Apollo's
            docker_base.sh matches container names by substring, so w1 would
            also match w10.
    """
    root = Path(apollo_root or CONFIG.APOLLO_ROOT)
    ctn = DeFTContainer(str(root), user)
    # The flags must be written into the checkout this run actually mounts as
    # /apollo, not into the one CONFIG happens to name. Concurrent workers each
    # own a checkout, so defaulting to CONFIG.APOLLO_ROOT edited a planning.conf
    # no container was reading and every replay silently fell back to the
    # compiled gflag defaults.
    conf_path = root / 'modules/planning/conf/planning.conf'

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
    with planning_flags(flags or {}, conf_path):
        if flags:
            applied = ' '.join(f'{k}={v}' for k, v in sorted(flags.items()))
            print(f'Applied planning flags: {applied}')
        ctn.deft_coverage(show_container_output=show_container_output)

    if save_report:
        if report_dir.exists():
            shutil.rmtree(report_dir)

        print('Saving coverage report...')
        ctn.save_genhtml(report_dir)

    tracefile = Path(lcov_path) if lcov_path else report_dir / 'coverage.dat'
    if not ctn.save_lcov(tracefile):
        raise SystemExit(
            'No LCOV tracefile was produced inside the container; '
            're-run with --show-container-output to see what went wrong.'
        )

    # After the tracefile, so a run that fails its corruption check below has
    # still left its counters behind to be examined.
    for kind, destination in (('gcda', gcda_path), ('gcno', gcno_path)):
        if destination is None:
            continue
        if not ctn.save_gcov_archive(kind, Path(destination)):
            print(
                f'Warning: no {kind} archive was produced inside the '
                'container; raw coverage data was not saved for this record.'
            )

    corrupt = find_corrupt_sources(tracefile, Path(apollo_root or CONFIG.APOLLO_ROOT))
    if corrupt:
        shown = '\n  '.join(corrupt[:5])
        more = f'\n  ... and {len(corrupt) - 5} more' if len(corrupt) > 5 else ''
        raise SystemExit(
            f'{tracefile} records coverage for lines that do not exist in '
            f'{len(corrupt)} source file(s):\n  {shown}{more}\n'
            'The instrumented test was very likely interrupted, leaving gcov '
            'counters half-written. Re-run to recompute this record.'
        )

    if keep_container:
        print('Keeping DeFT container running...')
    else:
        ctn.stop()
        ctn.remove()

    if save_report:
        if not report_dir.exists():
            raise SystemExit(
                'Coverage report was not produced inside the container; '
                're-run with --show-container-output to see what went wrong.'
            )

        print(f'Coverage report saved to {report_dir / "index.html"}')

    print(f'LCOV tracefile saved to {tracefile}')


def main(parser):
    parser.add_argument(
        'record',
        nargs='?',
        default=None,
        help='Scenario record to extract module tests from before computing '
        'coverage. Omit to reuse the frames already in --frames-dir',
    )

    parser.add_argument(
        '--frames-dir',
        default='out/testdata',
        help='Directory holding the extracted frames: read from when a record '
        'is not given, written to when one is',
    )

    parser.add_argument(
        '--impl',
        default='apollo',
        choices=sorted(IMPLEMENTATIONS),
        help='Implementation used to reconstruct frames when a record is '
        'given. Use "log" for records from an Apollo carrying the DeFT '
        'instrumentation',
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
        '--planning-flag',
        action='append',
        default=[],
        metavar='NAME=VALUE',
        help='Planning gflag to write into planning.conf for this run and '
        'restore afterwards; repeatable. Use this to reproduce the '
        'configuration the scenario was originally executed under',
    )

    parser.add_argument(
        '--lcov-out',
        default=None,
        help='Where to write the raw LCOV tracefile '
        '(default: coverage.dat inside --report-dir)',
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

        if args.record is not None:
            record = Path(args.record)
            if not record.exists():
                parser.error('Scenario record file does not exist')
            run_extract(record, frames_dir, map_name=args.map, impl=args.impl)
        elif not frames_dir.exists():
            parser.error('Frames directory does not exist')

        try:
            flags = dict(parse_flag(f) for f in args.planning_flag)
        except ValueError as e:
            parser.error(f'invalid --planning-flag: {e}')

        run_coverage(
            frames_dir,
            report_dir,
            map_name=args.map,
            set_map=not args.no_set_map,
            keep_container=args.keep_container,
            show_container_output=args.show_container_output,
            flags=flags,
            lcov_path=Path(args.lcov_out) if args.lcov_out else None,
        )

    parser.set_defaults(func=handler)
