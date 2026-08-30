"""Cumulative planning coverage over directories of scenario records.

A test generation technique produces a directory of scenario records. What is
interesting about such a directory is not any single record but what the whole
set reaches together, and how that compares against another technique's set.

This module runs `deft coverage` over every record in each configured
directory, keeping one tracefile per record, and unions them into a cumulative
tracefile per directory. Coverage of separate records can be unioned precisely
because a tracefile is line-addressed data rather than a rendering: the union
counts a line as covered when any record covered it.

Directories are configured by name, so the reported numbers say which technique
they belong to.
"""

import hashlib
import json
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml
from rich.console import Console
from rich.table import Table

from config import CONFIG
from deft.coverage import run_coverage
from deft.deft_container import DeFTContainer
from deft.extract import IMPLEMENTATIONS, run_extract
from deft.planning_flags import parse_flag

DEFAULT_GLOB = '*.00000'

# `lcov --summary` renders one of these per metric, or "no data found" when the
# tracefile carries nothing for it.
SUMMARY_PATTERN = re.compile(
    r'^\s*(lines|functions|branches)\.*:\s+'
    r'(?P<pct>[\d.]+)%\s+\((?P<hit>\d+) of (?P<total>\d+)',
    re.MULTILINE,
)


@dataclass
class Technique:
    """One named directory of scenario records."""

    name: str
    directory: Path

    @property
    def slug(self) -> str:
        """Filesystem-safe form of the name, used for output directories."""
        return re.sub(r'[^A-Za-z0-9._-]+', '_', self.name).strip('_') or 'unnamed'


@dataclass
class TechniqueResult:
    """What a technique's records covered, together."""

    technique: Technique
    tracefiles: List[Path] = field(default_factory=list)
    failures: List[str] = field(default_factory=list)
    cumulative: Optional[Path] = None
    summary: Dict[str, Dict[str, int]] = field(default_factory=dict)


def parse_summary(tracefile: Path) -> Dict[str, Dict[str, int]]:
    """
    Read the coverage rates of a tracefile.

    Args:
        tracefile (Path): The LCOV tracefile to summarize.

    Returns:
        Dict[str, Dict[str, int]]: Hit and total counts per metric.
    """
    result = subprocess.run(
        [
            'lcov',
            '--summary',
            str(tracefile),
            '--rc',
            'lcov_branch_coverage=1',
        ],
        capture_output=True,
        text=True,
    )
    # lcov writes the summary to stderr in some versions and stdout in others.
    output = result.stdout + result.stderr

    summary = {}
    for match in SUMMARY_PATTERN.finditer(output):
        summary[match.group(1)] = {
            'hit': int(match.group('hit')),
            'total': int(match.group('total')),
            'percent': float(match.group('pct')),
        }
    return summary


def union_tracefiles(tracefiles: List[Path], output: Path) -> bool:
    """
    Union per-record tracefiles into one cumulative tracefile.

    Args:
        tracefiles (List[Path]): The tracefiles to union.
        output (Path): Where to write the cumulative tracefile.

    Returns:
        bool: True when the union was produced.
    """
    if not tracefiles:
        return False

    output.parent.mkdir(parents=True, exist_ok=True)
    command = ['lcov']
    for tracefile in tracefiles:
        command += ['--add-tracefile', str(tracefile)]
    # Branch records are dropped from the output unless this is set, which
    # would silently cost the union its branch data.
    command += ['--rc', 'lcov_branch_coverage=1', '--output-file', str(output)]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f'lcov failed to union tracefiles: {result.stderr.strip()}')
        return False
    return output.exists()


def render_cumulative(tracefile: Path, report_dir: Path) -> bool:
    """
    Render a cumulative tracefile to HTML.

    The tracefile holds workspace-relative paths, so this runs from the Apollo
    checkout on the host, where those paths resolve to the planning sources.

    Args:
        tracefile (Path): The cumulative tracefile to render.
        report_dir (Path): Directory to write the HTML report to.

    Returns:
        bool: True when the report was produced.
    """
    if shutil.which('genhtml') is None:
        print('genhtml is not installed on this host; skipping HTML report')
        return False

    if report_dir.exists():
        shutil.rmtree(report_dir)

    result = subprocess.run(
        [
            'genhtml',
            '--branch-coverage',
            '--rc',
            'genhtml_branch_coverage=1',
            '--ignore-errors',
            'source',
            '--output',
            str(report_dir.resolve()),
            str(tracefile.resolve()),
        ],
        cwd=str(Path(CONFIG.APOLLO_ROOT)),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f'genhtml failed: {result.stderr.strip()}')
        return False
    return True


def find_records(
    directory: Path, pattern: str, limit: Optional[int] = None
) -> List[Path]:
    """
    List the scenario records of a directory, including its subdirectories.

    Args:
        directory (Path): Directory to search.
        pattern (str): Glob matching the record files.
        limit (Optional[int]): Keep at most this many records. The order is
            stable, so a limited run covers the same records every time.

    Returns:
        List[Path]: Matching records, in a stable order.
    """
    records = sorted(p for p in directory.rglob(pattern) if p.is_file())
    return records[:limit] if limit is not None else records


def record_key(directory: Path, record: Path) -> str:
    """
    Name a record uniquely within the directory it was found under.

    The search is recursive, so two records in different subdirectories can
    share a file name. A hash of the record's path guarantees the tracefiles
    stay apart, whatever the tree looks like; keying on the file name alone
    would let one record overwrite another's tracefile, and the overwritten
    record would then look already covered on a resumed run. The file name is
    kept as a prefix so the output remains readable.

    The hash covers the path relative to the search directory rather than the
    absolute one, so moving or renaming the directory does not change the keys
    and a resumed batch still finds the tracefiles it already computed.

    Args:
        directory (Path): The directory the record was found under.
        record (Path): The record file.

    Returns:
        str: A filesystem-safe key for the record.
    """
    try:
        relative = record.relative_to(directory)
    except ValueError:
        relative = Path(record.name)

    digest = hashlib.sha1(str(relative).encode()).hexdigest()[:8]
    name = re.sub(r'[^A-Za-z0-9._-]+', '_', relative.with_suffix('').name).strip('_')
    return f'{name}-{digest}' if name else digest


def run_coverage_batch(
    techniques: List[Technique],
    out_dir: Path,
    work_dir: Path,
    pattern: str = DEFAULT_GLOB,
    impl: str = 'log',
    map_name: Optional[str] = None,
    set_map: bool = True,
    flags: Optional[Dict[str, str]] = None,
    force: bool = False,
    limit: Optional[int] = None,
    keep_container: bool = False,
    show_container_output: bool = False,
) -> List[TechniqueResult]:
    """
    Compute cumulative planning coverage for each configured directory.

    Args:
        techniques (List[Technique]): Named directories of scenario records.
        out_dir (Path): Directory to write tracefiles and reports to.
        work_dir (Path): Directory to extract module tests into.
        pattern (str): Glob matching the record files in each directory.
        impl (str): Implementation used to reconstruct frames.
        map_name (Optional[str]): HD map to configure for every record,
            overriding the one detected during extraction.
        set_map (bool): Whether to configure Apollo's HD map at all.
        flags (Optional[Dict[str, str]]): Planning gflags applied to each run.
        force (bool): Recompute records whose tracefile already exists.
        limit (Optional[int]): Cover at most this many records per directory,
            for quickly trying a configuration out before running it in full.
        keep_container (bool): Leave the container running at the end.
        show_container_output (bool): Show container output for each run.

    Returns:
        List[TechniqueResult]: What each technique's records covered.
    """
    results = []

    total_records = sum(
        len(find_records(t.directory, pattern, limit)) for t in techniques
    )
    completed = 0

    for technique in techniques:
        result = TechniqueResult(technique=technique)
        results.append(result)

        records = find_records(technique.directory, pattern, limit)
        available = len(find_records(technique.directory, pattern))
        if not records:
            print(
                f'[{technique.name}] no records matching {pattern!r} under '
                f'{technique.directory}'
            )
            continue

        limited = '' if limit is None else f' (limited from {available})'
        print(f'[{technique.name}] {len(records)} record(s) to cover{limited}')

        technique_out = out_dir / technique.slug
        records_out = technique_out / 'records'
        records_out.mkdir(parents=True, exist_ok=True)

        for record in records:
            completed += 1
            key = record_key(technique.directory, record)
            tracefile = records_out / f'{key}.dat'
            label = f'({completed}/{total_records}) {technique.name}/{key}'

            if tracefile.exists() and not force:
                print(f'{label}: reusing existing tracefile')
                result.tracefiles.append(tracefile)
                continue

            print(f'{label}: extracting and covering')
            frames_dir = work_dir / technique.slug / key

            try:
                run_extract(record, frames_dir, map_name=map_name, impl=impl)
                run_coverage(
                    frames_dir,
                    technique_out / 'unused_report',
                    map_name=map_name,
                    set_map=set_map,
                    # The container is reused across every record and stopped
                    # once the whole batch is done.
                    keep_container=True,
                    show_container_output=show_container_output,
                    flags=flags,
                    lcov_path=tracefile,
                    save_report=False,
                )
                result.tracefiles.append(tracefile)
            except Exception as e:  # noqa: BLE001 - one bad record must not
                # abandon a batch that may take hours.
                print(f'{label}: FAILED: {e}')
                result.failures.append(f'{record.name}: {e}')
            finally:
                shutil.rmtree(frames_dir, ignore_errors=True)

        cumulative = technique_out / 'cumulative.dat'
        if union_tracefiles(result.tracefiles, cumulative):
            result.cumulative = cumulative
            result.summary = parse_summary(cumulative)
            render_cumulative(cumulative, technique_out / 'genhtml')

    if not keep_container:
        ctn = DeFTContainer(str(Path(CONFIG.APOLLO_ROOT)), 'deft')
        if ctn.is_running():
            print('Stopping DeFT container...')
            ctn.stop()
            ctn.remove()

    return results


def report(results: List[TechniqueResult], out_dir: Path):
    """
    Print the cumulative coverage of each technique and write it to disk.

    Args:
        results (List[TechniqueResult]): What each technique covered.
        out_dir (Path): Directory the batch wrote its output to.
    """
    console = Console()

    table = Table(title='Cumulative planning coverage')
    table.add_column('Technique')
    table.add_column('Records', justify='right')
    table.add_column('Lines', justify='right')
    table.add_column('Functions', justify='right')
    table.add_column('Branches', justify='right')

    def cell(summary: Dict[str, Dict[str, int]], metric: str) -> str:
        data = summary.get(metric)
        if not data:
            return '-'
        return f'{data["percent"]:.1f}% ({data["hit"]}/{data["total"]})'

    for result in results:
        table.add_row(
            result.technique.name,
            str(len(result.tracefiles)),
            cell(result.summary, 'lines'),
            cell(result.summary, 'functions'),
            cell(result.summary, 'branches'),
        )

    console.print(table)

    for result in results:
        if result.failures:
            console.print(
                f'[red]{result.technique.name}: '
                f'{len(result.failures)} record(s) failed[/red]'
            )
            for failure in result.failures:
                console.print(f'  {failure}')

    summary_path = out_dir / 'summary.json'
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with open(summary_path, 'w') as fp:
        json.dump(
            [
                {
                    'name': r.technique.name,
                    'directory': str(r.technique.directory),
                    'records': len(r.tracefiles),
                    'cumulative': str(r.cumulative) if r.cumulative else None,
                    'coverage': r.summary,
                    'failures': r.failures,
                }
                for r in results
            ],
            fp,
            indent=2,
        )
        fp.write('\n')

    console.print(f'Summary written to {summary_path}')
    for result in results:
        if result.cumulative:
            console.print(
                f'{result.technique.name}: {result.cumulative} '
                f'(report: {result.cumulative.parent / "genhtml" / "index.html"})'
            )


def load_techniques(config_path: Path) -> List[Technique]:
    """
    Read the configured directories from a config file.

    The file is YAML, which also covers JSON. It holds a list of
    ``{name, dir}`` entries, either at the top level or under a ``techniques``
    key, and a mapping of name to directory is accepted as a shorthand.

    Args:
        config_path (Path): Path of the config file.

    Returns:
        List[Technique]: The configured directories.
    """
    with open(config_path) as fp:
        config = yaml.safe_load(fp)

    if config is None:
        raise ValueError(f'{config_path} is empty')

    if isinstance(config, dict):
        entries = config.get('techniques', config)
    else:
        entries = config

    # Shorthand: a plain mapping of name to directory.
    if isinstance(entries, dict):
        entries = [
            {'name': name, 'dir': directory}
            for name, directory in entries.items()
        ]

    techniques = []
    for entry in entries:
        if not isinstance(entry, dict) or 'name' not in entry or 'dir' not in entry:
            raise ValueError(
                f'{config_path}: each technique needs a name and a dir, '
                f'got {entry!r}'
            )
        directory = Path(str(entry['dir'])).expanduser()
        techniques.append(Technique(name=str(entry['name']), directory=directory))

    if not techniques:
        raise ValueError(f'{config_path} lists no techniques')

    return techniques


def parse_dir_argument(value: str) -> Technique:
    """
    Parse a ``NAME=PATH`` command line directory.

    Args:
        value (str): The argument to parse.

    Returns:
        Technique: The named directory.
    """
    name, sep, path = value.partition('=')
    if not sep or not name.strip() or not path.strip():
        raise ValueError(f'expected NAME=PATH, got {value!r}')
    return Technique(name=name.strip(), directory=Path(path.strip()).expanduser())


def main(parser):
    parser.add_argument(
        '--config',
        default=None,
        help='YAML (or JSON) file listing the named record directories to '
        'cover; see README for the format',
    )

    parser.add_argument(
        '--dir',
        action='append',
        default=[],
        metavar='NAME=PATH',
        dest='dirs',
        help='Named directory of scenario records; repeatable. Use instead of '
        '--config for one-off runs',
    )

    parser.add_argument(
        '--glob',
        default=DEFAULT_GLOB,
        help=f'Glob matching the record files, searched recursively under '
        f'each directory (default: {DEFAULT_GLOB})',
    )

    parser.add_argument(
        '--impl',
        default='log',
        choices=sorted(IMPLEMENTATIONS),
        help='Implementation used to reconstruct frames (default: log, for '
        'records from an Apollo carrying the DeFT instrumentation)',
    )

    parser.add_argument(
        '--out-dir',
        default='out/coverage_batch',
        help='Directory to write per-record tracefiles, cumulative tracefiles '
        'and reports to',
    )

    parser.add_argument(
        '--work-dir',
        default='out/batch_testdata',
        help='Directory to extract module tests into; each record is removed '
        'again once it has been covered',
    )

    parser.add_argument(
        '--map',
        default=None,
        help='HD map to configure for every record, overriding the one '
        'detected during extraction',
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
        help='Planning gflag to apply to every run; repeatable',
    )

    parser.add_argument(
        '--force',
        action='store_true',
        help='Recompute records whose tracefile already exists, instead of '
        'reusing it',
    )

    parser.add_argument(
        '--limit',
        type=int,
        default=None,
        metavar='N',
        help='Cover at most N records per directory, for quickly trying a '
        'configuration out before running it in full',
    )

    parser.add_argument(
        '--keep-container',
        action='store_true',
        help='Leave the DeFT container running after the batch finishes',
    )

    parser.add_argument(
        '--show-container-output',
        action='store_true',
        help='Show the output of each coverage run inside the container',
    )

    def handler(args):
        techniques = []

        if args.config:
            config_path = Path(args.config)
            if not config_path.exists():
                parser.error('Config file does not exist')
            try:
                techniques += load_techniques(config_path)
            except (ValueError, KeyError, yaml.YAMLError) as e:
                parser.error(f'invalid --config: {e}')

        for value in args.dirs:
            try:
                techniques.append(parse_dir_argument(value))
            except ValueError as e:
                parser.error(f'invalid --dir: {e}')

        if not techniques:
            parser.error('No record directories given; pass --config or --dir')

        for technique in techniques:
            if not technique.directory.is_dir():
                parser.error(
                    f'Record directory does not exist: {technique.directory}'
                )

        try:
            flags = dict(parse_flag(f) for f in args.planning_flag)
        except ValueError as e:
            parser.error(f'invalid --planning-flag: {e}')

        out_dir = Path(args.out_dir)
        results = run_coverage_batch(
            techniques,
            out_dir,
            Path(args.work_dir),
            pattern=args.glob,
            impl=args.impl,
            map_name=args.map,
            set_map=not args.no_set_map,
            flags=flags,
            force=args.force,
            limit=args.limit,
            keep_container=args.keep_container,
            show_container_output=args.show_container_output,
        )
        report(results, out_dir)

    parser.set_defaults(func=handler)
