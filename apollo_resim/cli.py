import argparse
import string
from pathlib import Path

from nanoid import generate
from rich_argparse import RichHelpFormatter

from apollo_resim import re_simulate
from config import CONFIG
from deft.map_config import get_apollo_map, install_map, set_apollo_map
from deft.map_detect import MapDetectionError, describe, detect_map


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
        default=None,
        help=(
            "Map name (must exist under data/maps/<map_name>/base_map.bin). "
            "Detected from the source record when omitted."
        ),
    )

    args = parser.parse_args()

    src = Path(args.src_record)
    dst = Path(args.dst_record)

    if not src.exists():
        parser.error("Source record file does not exist")

    if dst.exists():
        parser.error("Destination file already exists")

    map_name = args.map
    if map_name is None:
        print("Detecting HD map ...")
        try:
            result = detect_map(src)
            print(describe(result))
            map_name = result.map_name
        except MapDetectionError as e:
            parser.error(f"HD map detection failed: {e}")
        if map_name is None:
            parser.error(
                "HD map could not be detected from the source record, "
                "pass --map explicitly"
            )

    map_dir = Path(CONFIG.PROJECT_ROOT, "data", "maps", map_name)
    map_bin = Path(map_dir, "base_map.bin")

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

    # Apollo resolves the replayed route against whichever map --map_dir points
    # at, so the container has to be configured with the same map that is
    # loaded here.
    if get_apollo_map(CONFIG.APOLLO_ROOT) != map_name:
        try:
            install_map(CONFIG.APOLLO_ROOT, map_dir)
            set_apollo_map(CONFIG.APOLLO_ROOT, map_name)
        except FileNotFoundError as e:
            parser.error(str(e))
    print(f"Apollo HD map set to {map_name}")

    re_simulate(
        apollo_root=CONFIG.APOLLO_ROOT,
        container_name=generate(alphabet=string.ascii_letters, size=10),
        start_script=str(start_script),
        map_bin=str(map_bin),
        src=str(src),
        dst=str(dst),
    )
