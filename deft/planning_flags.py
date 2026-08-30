import re
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, Optional

from config import CONFIG

#: A gflag line in planning.conf, e.g. ``--enable_scenario_pull_over=true``.
_FLAG_RE = re.compile(r'^\s*--([A-Za-z_][A-Za-z0-9_]*)\s*=')

#: Flags absent from planning.conf fall back to the value compiled into
#: planning_gflags.cc, so a scenario that relied on a non-default value must
#: have it written out explicitly before the module tests run.
PLANNING_CONF = Path(CONFIG.APOLLO_ROOT, 'modules/planning/conf/planning.conf')

OriginalState = Dict[str, Optional[str]]


def parse_flag(text: str):
    """
    Parse a ``name=value`` flag argument.

    Args:
        text (str): The flag argument, with or without a leading ``--``.

    Returns:
        A ``(name, value)`` pair.

    Raises:
        ValueError: If the argument is not of the form ``name=value``.
    """
    if '=' not in text:
        raise ValueError(f'expected name=value, got {text!r}')
    name, value = text.split('=', 1)
    name = name.strip().lstrip('-')
    if not name:
        raise ValueError(f'missing flag name in {text!r}')
    return name, value.strip()


def apply_flags(flags: Dict[str, str], conf_path: Path = PLANNING_CONF) -> OriginalState:
    """
    Overwrite or append flags in planning.conf and return the original state.

    Args:
        flags (Dict[str, str]): Flag names (without ``--``) mapped to values.
        conf_path (Path): The planning.conf to edit.

    Returns:
        Original state suitable for passing to :func:`restore_flags`.
    """
    if not flags:
        return {}

    lines = conf_path.read_text().splitlines()

    line_indices: Dict[str, int] = {}
    for i, line in enumerate(lines):
        m = _FLAG_RE.match(line)
        if m:
            line_indices[m.group(1)] = i

    original: OriginalState = {}
    for name, value in flags.items():
        new_line = f'--{name}={value}'
        if name in line_indices:
            idx = line_indices[name]
            original[name] = lines[idx]
            lines[idx] = new_line
        else:
            original[name] = None
            lines.append(new_line)

    conf_path.write_text('\n'.join(lines) + '\n')
    return original


def restore_flags(original: OriginalState, conf_path: Path = PLANNING_CONF) -> None:
    """
    Undo a previous :func:`apply_flags`.

    Args:
        original (OriginalState): The value returned by :func:`apply_flags`.
        conf_path (Path): The planning.conf to restore.
    """
    if not original:
        return

    lines = conf_path.read_text().splitlines()
    keep = []
    for line in lines:
        m = _FLAG_RE.match(line)
        if m and m.group(1) in original:
            name = m.group(1)
            if original[name] is not None:
                keep.append(original[name])
            # appended flags are dropped
        else:
            keep.append(line)

    conf_path.write_text('\n'.join(keep) + '\n')


@contextmanager
def planning_flags(flags: Dict[str, str], conf_path: Path = PLANNING_CONF):
    """
    Apply flags to planning.conf for the duration of the block.

    Args:
        flags (Dict[str, str]): Flag names (without ``--``) mapped to values.
        conf_path (Path): The planning.conf to edit.
    """
    original = apply_flags(flags, conf_path)
    try:
        yield
    finally:
        restore_flags(original, conf_path)
