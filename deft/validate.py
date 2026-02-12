from pathlib import Path

from apollo_modules.modules.planning.proto.planning_pb2 import ADCTrajectory
from deft.representation.trajectory import euclidean_distance
from deft.utils import get_trajectory_from_planning_bin


def run_verify(outputs_dir: Path):
    """
    Verify reproduced planning trajectories.

    Parameters
    ----------
    outputs_dir : Path
        Directory containing execution outputs (e.g., planning.bin files).
    """

    reproduce_errors = []

    testdata_out = Path(outputs_dir)
    print('Comparing trajectories...')
    for test_index in testdata_out.iterdir():
        if test_index.is_dir():
            output = get_trajectory_from_planning_bin(test_index / 'deft.bin')
            with open(test_index / 'deft.bin', 'rb') as f:
                ob = ADCTrajectory()
                ob.ParseFromString(f.read())
                with open(test_index / 'deft.bin.txt', 'w') as f_txt:
                    f_txt.write(str(ob))

            expected = get_trajectory_from_planning_bin(test_index / 'planning.bin')
            with open(test_index / 'planning.bin', 'rb') as f:
                ob = ADCTrajectory()
                ob.ParseFromString(f.read())
                with open(test_index / 'planning.bin.txt', 'w') as f_txt:
                    f_txt.write(str(ob))

            dist = euclidean_distance(output, expected)
            reproduce_errors.append(dist)

    # print total number of reproduced trajectories
    print('Total reproduced trajectories:', len(reproduce_errors))

    # print min, max, avg reproduce error
    print('Min reproduce error:', min(reproduce_errors))
    print('Max reproduce error:', max(reproduce_errors))
    print('Avg reproduce error:', sum(reproduce_errors) / len(reproduce_errors))


def main(parser):
    parser.add_argument(
        "--outputs-dir",
        default="out/testdata_out",
        help="Directory containing execution outputs",
    )

    def handler(args):
        outputs_dir = Path(args.outputs_dir)

        if not outputs_dir.exists():
            parser.error("Outputs directory does not exist")

        run_verify(outputs_dir)

    parser.set_defaults(func=handler)
