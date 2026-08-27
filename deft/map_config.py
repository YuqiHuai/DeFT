"""Configuration of the HD map used by an Apollo installation.

Apollo selects its HD map through the ``--map_dir`` flag in
``modules/common/data/global_flagfile.txt``. Both the module test runner
(``deft execute``) and the re-simulation CLI (``apollo_resim``) have to point
Apollo at the map that produced the record they work on, so the flagfile
handling lives here and is shared by both.

Writing the flag replaces any previously configured map instead of appending a
new one: gflags lets the last occurrence win, so appending works but silently
grows the flagfile and makes the active map hard to read back.
"""

import shutil
from pathlib import Path
from typing import List, Optional

MAP_DIR_FLAG_PREFIX = '--map_dir='
CONTAINER_MAP_DATA_DIR = '/apollo/modules/map/data'


def map_data_dir(apollo_root: Path) -> Path:
    """
    Get the directory holding the HD maps installed into Apollo.

    Args:
        apollo_root (Path): Root directory of the Apollo installation.

    Returns:
        Path: The map data directory.
    """
    return Path(apollo_root, 'modules', 'map', 'data')


def global_flagfile(apollo_root: Path) -> Path:
    """
    Get the Apollo flagfile that holds the active map directory.

    Args:
        apollo_root (Path): Root directory of the Apollo installation.

    Returns:
        Path: The global flagfile.
    """
    return Path(apollo_root, 'modules', 'common', 'data', 'global_flagfile.txt')


def installed_maps(apollo_root: Path) -> List[str]:
    """
    List the HD maps installed into Apollo.

    Args:
        apollo_root (Path): Root directory of the Apollo installation.

    Returns:
        List[str]: Names of the installed maps.
    """
    data_dir = map_data_dir(apollo_root)
    if not data_dir.is_dir():
        return []
    return sorted(d.name for d in data_dir.iterdir() if d.is_dir())


def get_apollo_map(apollo_root: Path) -> Optional[str]:
    """
    Get the HD map Apollo is currently configured to use.

    Args:
        apollo_root (Path): Root directory of the Apollo installation.

    Returns:
        Optional[str]: The map name, or None when no map is configured.
    """
    flagfile = global_flagfile(apollo_root)
    if not flagfile.exists():
        return None

    map_dir = None
    with open(flagfile, 'r') as fp:
        for line in fp:
            line = line.strip()
            if line.startswith(MAP_DIR_FLAG_PREFIX):
                # Later occurrences override earlier ones.
                map_dir = line[len(MAP_DIR_FLAG_PREFIX) :].strip().rstrip('/')
    return Path(map_dir).name if map_dir else None


def install_map(apollo_root: Path, map_dir: Path):
    """
    Copy an HD map into Apollo's map data directory if it is missing.

    Args:
        apollo_root (Path): Root directory of the Apollo installation.
        map_dir (Path): Source directory of the HD map.

    Raises:
        FileNotFoundError: If the source map directory does not exist.
    """
    if not map_dir.is_dir():
        raise FileNotFoundError(f'HD map not found: {map_dir}')

    target = Path(map_data_dir(apollo_root), map_dir.name)
    if target.exists():
        return

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(map_dir, target)


def set_apollo_map(apollo_root: Path, map_name: str):
    """
    Point Apollo at an installed HD map.

    Any previously configured map directory is replaced, so that repeated calls
    do not accumulate conflicting flags in the flagfile.

    Args:
        apollo_root (Path): Root directory of the Apollo installation.
        map_name (str): The name of the map to use.

    Raises:
        FileNotFoundError: If Apollo or the requested map is not installed.
    """
    flagfile = global_flagfile(apollo_root)
    if not flagfile.exists():
        raise FileNotFoundError(
            f'Apollo flagfile not found: {flagfile}. '
            'Run scripts/install_apollo.sh first.'
        )

    if not Path(map_data_dir(apollo_root), map_name).is_dir():
        available = ', '.join(installed_maps(apollo_root)) or 'none'
        raise FileNotFoundError(
            f"Map '{map_name}' is not installed under {map_data_dir(apollo_root)}. "
            f'Available maps: {available}. '
            'Run scripts/install_hd_maps.sh to install the bundled maps.'
        )

    with open(flagfile, 'r') as fp:
        lines = fp.read().splitlines()

    kept = [
        line for line in lines if not line.strip().startswith(MAP_DIR_FLAG_PREFIX)
    ]
    while kept and not kept[-1].strip():
        kept.pop()
    kept.append('')
    kept.append(f'{MAP_DIR_FLAG_PREFIX}{CONTAINER_MAP_DATA_DIR}/{map_name}')

    with open(flagfile, 'w') as fp:
        fp.write('\n'.join(kept) + '\n')
