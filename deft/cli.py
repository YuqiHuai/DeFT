import argparse

from rich_argparse import RichHelpFormatter

from deft.coverage import main as coverage_main
from deft.coverage_batch import main as coverage_batch_main
from deft.detect import main as detect_main
from deft.execute import main as execute_main
from deft.extract import main as extract_main
from deft.validate import main as validate_main


def main():
    parser = argparse.ArgumentParser(
        description='DeFT CLI',
        formatter_class=RichHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # Extract command
    extract_parser = subparsers.add_parser(
        'extract', help='Extract module tests from scenario record'
    )
    extract_main(extract_parser)

    # Execute command
    execute_parser = subparsers.add_parser(
        'execute', help='Execute extracted module tests'
    )
    execute_main(execute_parser)

    # Detect map command
    detect_parser = subparsers.add_parser(
        'detect-map', help='Detect the HD map used by a scenario record'
    )
    detect_main(detect_parser)

    # Coverage command
    coverage_parser = subparsers.add_parser(
        'coverage', help='Compute planning coverage of extracted module tests'
    )
    coverage_main(coverage_parser)

    # Batch coverage command
    coverage_batch_parser = subparsers.add_parser(
        'coverage-batch',
        help='Compute cumulative planning coverage for directories of records',
    )
    coverage_batch_main(coverage_batch_parser)

    # Validate command
    validate_parser = subparsers.add_parser(
        'validate', help='Validate extracted module tests'
    )
    validate_main(validate_parser)

    args = parser.parse_args()
    args.func(args)
