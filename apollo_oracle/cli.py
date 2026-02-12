import argparse
import json
from pathlib import Path
from typing import List

from rich_argparse import RichHelpFormatter

from apollo_oracle.core import OracleExtension, OracleExtensionManager, analyze_record
from apollo_oracle.utils.map_service import load_map_service
from apollo_oracle.utils.vehicle_param import VehicleParam


def set_up_parser():
    parser = argparse.ArgumentParser(
        description='Apollo scenario analysis with extendable oracles',
        formatter_class=RichHelpFormatter,
    )

    parser.add_argument(
        '-a',
        '--all',
        default=False,
        action='store_true',
        help='Use all available oracles',
    )
    parser.add_argument(
        '-i',
        '--include',
        default=[],
        nargs='+',
        help='Specify oracles to be included in the analysis',
    )
    parser.add_argument(
        '-e',
        '--exclude',
        default=[],
        nargs='+',
        help='Specify oracles to be excluded in the analysis',
    )
    parser.add_argument(
        '-v',
        '--vehicle',
        type=str,
        nargs=1,
        required=True,
        help='Specify path of vehicle_param protobuf file',
    )
    parser.add_argument(
        '-m',
        '--map',
        type=str,
        nargs=1,
        required=True,
        help='Specify path of the HD map',
    )

    parser.add_argument('scenario', help='Scenario to analyze')
    parser.add_argument('out', help='Location to save analysis report')

    return parser


def main():
    # oracle_manager = OracleExtensionManager()
    # print(oracle_manager.available_extensions)

    parser = set_up_parser()
    oracle_manager = OracleExtensionManager()
    oracle_manager.extend_cli_parser(parser)

    # Verify arguments
    args = parser.parse_args()
    args_dict = vars(args)

    all_oracle_active = args_dict.get('all')
    included_oracles = args_dict.get('include')
    excluded_oracles = args_dict.get('exclude')
    vehicle_param_file = Path(args_dict.get('vehicle')[0])
    map_file = Path(args_dict.get('map')[0])

    record_file = Path(args_dict.get('scenario'))
    out_file = Path(args_dict.get('out'))

    if all_oracle_active:
        if len(excluded_oracles) > 0:
            parser.error(
                'Command line option --all and --exclude are mutually exclusive'
            )

    if len(included_oracles) > 0 and len(excluded_oracles) > 0:
        for item in included_oracles:
            if item in excluded_oracles:
                parser.error(
                    f'Included and excluded oracles are mutually exclusive ({item})'
                )

    if not vehicle_param_file.exists():
        parser.error('Specified vehicle param file does not exist!')

    if not map_file.exists():
        parser.error('Specified map file does not exist!')

    if not record_file.exists():
        parser.error('Scenario record file does not exist!')

    if out_file.exists():
        parser.error('Output file already exists!')

    # load dependencies and run tests
    map_service = load_map_service(map_file)
    vehicle_param = VehicleParam.load_from_file(vehicle_param_file)

    active_oracles = oracle_manager.get_active_extensions(
        all_oracle_active, included_oracles, excluded_oracles
    )
    oracle_instances: List[OracleExtension] = [
        e(map_service, vehicle_param, args_dict) for e in active_oracles
    ]

    print('Active extensions %s' % [e.get_name() for e in active_oracles])
    violations = analyze_record(oracle_instances, record_file)
    print(violations)
    print(f'Writing results to {out_file}')
    with open(out_file, 'w') as fp:
        json.dump([v.asdict() for v in violations], fp)
