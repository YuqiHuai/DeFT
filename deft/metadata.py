"""Metadata stored alongside extracted module tests.

``deft extract`` records the HD map that the scenario record was produced on so
that ``deft execute`` can configure Apollo with the same map without the user
having to remember it. The file lives next to the numbered frame directories
and is ignored by the test runner, which only looks at ``<index>/planning.bin``.
"""

import json
from pathlib import Path
from typing import Optional

METADATA_FILENAME = 'deft_meta.json'


def metadata_path(frames_dir: Path) -> Path:
    """
    Get the path of the metadata file of an extraction directory.

    Args:
        frames_dir (Path): Directory containing the extracted frames.

    Returns:
        Path: Path of the metadata file.
    """
    return Path(frames_dir, METADATA_FILENAME)


def write_metadata(frames_dir: Path, metadata: dict):
    """
    Write extraction metadata into an extraction directory.

    Args:
        frames_dir (Path): Directory containing the extracted frames.
        metadata (dict): Metadata to store.
    """
    with open(metadata_path(frames_dir), 'w') as fp:
        json.dump(metadata, fp, indent=2)
        fp.write('\n')


def read_metadata(frames_dir: Path) -> dict:
    """
    Read extraction metadata from an extraction directory.

    Args:
        frames_dir (Path): Directory containing the extracted frames.

    Returns:
        dict: The stored metadata, or an empty dict when unavailable.
    """
    path = metadata_path(frames_dir)
    if not path.exists():
        return dict()
    try:
        with open(path, 'r') as fp:
            return json.load(fp)
    except (OSError, json.JSONDecodeError):
        return dict()


def read_map_name(frames_dir: Path) -> Optional[str]:
    """
    Read the HD map recorded for an extraction directory.

    Args:
        frames_dir (Path): Directory containing the extracted frames.

    Returns:
        Optional[str]: The map name, or None when it was not recorded.
    """
    return read_metadata(frames_dir).get('map')
