import argparse
import string
from pathlib import Path

from nanoid import generate
from rich_argparse import RichHelpFormatter

from apollo_resim import re_simulate
from config import CONFIG


def main():
    parser = argparse.ArgumentParser(
        description="Apollo record re-simulation CLI",
        formatter_class=RichHelpFormatter,
    )

    parser.add_argument("src_record", help="Source Apollo record file")
    parser.add_argument("dst_record", help="Destination output record file")

    parser.add_argument(
        "-m",
        "--map",
        required=True,
        help="Map name (must exist under data/maps/<map_name>/base_map.bin)",
    )

    args = parser.parse_args()

    src = Path(args.src_record)
    dst = Path(args.dst_record)

    if not src.exists():
        parser.error("Source record file does not exist")

    if dst.exists():
        parser.error("Destination file already exists")

    map_bin = Path(
        CONFIG.PROJECT_ROOT,
        "data",
        "maps",
        args.map,
        "base_map.bin",
    )

    if not map_bin.exists():
        parser.error(f"Map binary not found: {map_bin}")

    start_script = Path(
        CONFIG.APOLLO_ROOT,
        "docker",
        "scripts",
        "dev_start.sh",
    )

    if not start_script.exists():
        parser.error("Apollo start script not found")

    re_simulate(
        apollo_root=CONFIG.APOLLO_ROOT,
        container_name=generate(alphabet=string.ascii_letters, size=10),
        start_script=str(start_script),
        map_bin=str(map_bin),
        src=str(src),
        dst=str(dst),
    )
