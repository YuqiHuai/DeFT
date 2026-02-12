import argparse

from rich_argparse import RichHelpFormatter

from deft.execute import main as execute_main
from deft.extract import main as extract_main
from deft.validate import main as validate_main


def main():
    parser = argparse.ArgumentParser(
        description="DeFT CLI",
        formatter_class=RichHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Extract command
    extract_parser = subparsers.add_parser(
        "extract", help="Extract module tests from scenario record"
    )
    extract_main(extract_parser)

    # Execute command
    execute_parser = subparsers.add_parser(
        "execute", help="Execute extracted module tests"
    )
    execute_main(execute_parser)

    # Validate command
    validate_parser = subparsers.add_parser(
        "validate", help="Validate extracted module tests"
    )
    validate_main(validate_parser)

    args = parser.parse_args()
    args.func(args)
