import shutil
from pathlib import Path

from config import CONFIG
from deft.deft_container import DeFTContainer


def run_execute(frames_dir: Path, outputs_dir: Path):
    print("Starting DeFT container...")
    ctn = DeFTContainer(Path(CONFIG.APOLLO_ROOT), "deft")

    if not ctn.is_running():
        ctn.start()

    assert ctn.is_running()

    if outputs_dir.exists():
        shutil.rmtree(outputs_dir)

    print("Loading testdata into container...")
    ctn.load_testdata(frames_dir)

    print("Running DeFT tests...")
    ctn.deft_run_tests()

    print("Saving outputs...")
    ctn.save_testdata(outputs_dir)

    ctn.stop()
    ctn.remove()

    print(f"Outputs saved to {outputs_dir}")


def main(parser):
    parser.add_argument(
        "--frames-dir",
        default="out/testdata",
        help="Directory containing extracted frames",
    )

    parser.add_argument(
        "--outputs-dir",
        default="out/testdata_out",
        help="Directory to store execution outputs",
    )

    def handler(args):
        frames_dir = Path(args.frames_dir)
        outputs_dir = Path(args.outputs_dir)

        if not frames_dir.exists():
            parser.error("Frames directory does not exist")

        run_execute(frames_dir, outputs_dir)

    parser.set_defaults(func=handler)
