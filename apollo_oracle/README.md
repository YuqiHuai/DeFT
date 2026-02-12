# apollo_oracle

Apollo scenario analysis tool with extendable oracle plugins.

`apollo_oracle` analyzes Apollo record scenarios using a pluggable oracle system. It loads an HD map and vehicle parameters, activates selected oracle extensions, and outputs detected violations as a JSON report.

---

## Installation

### Requirements

- Python ≥ 3.10
- Poetry

### Install dependencies

```bash
poetry install
```

---

## Usage

Run the CLI using Poetry:

```bash
poetry run apollo_oracle [OPTIONS] <scenario> <out>
```

### Example

```bash
poetry run apollo_oracle \
  -v data/vehicle_params/Mkz_Example.txt \
  -m data/maps/borregas_ave/base_map.bin \
  data/test_scenario.00000 \
  out.json
```

---

## Arguments

| Argument   | Description |
|------------|------------|
| `scenario` | Path to the Apollo record file to analyze |
| `out`      | Path to the JSON output file (must not already exist) |

---

## Required Options

| Option | Description |
|--------|------------|
| `-v, --vehicle` | Path to vehicle parameter protobuf file |
| `-m, --map`     | Path to HD map file (e.g., `base_map.bin`) |

---

## Optional Flags

| Option | Description |
|--------|------------|
| `-a, --all` | Activate all available oracle extensions |
| `-i, --include <names...>` | Specify one or more oracles to include |
| `-e, --exclude <names...>` | Specify one or more oracles to exclude |

---

## Validation Rules

The CLI performs the following checks before running analysis:

- `--all` and `--exclude` are mutually exclusive.
- An oracle cannot be both included and excluded.
- Vehicle parameter file must exist.
- Map file must exist.
- Scenario record file must exist.
- Output file must **not** already exist.

If validation fails, the program exits with an error message.

---

## How It Works

1. Parses CLI arguments.
2. Loads the HD map.
3. Loads vehicle parameters.
4. Resolves active oracle extensions.
5. Runs scenario analysis.
6. Writes violations to the specified JSON file.

---

## Output Format

The output file is a JSON list of violation objects:

```json
[
  {
    "name": "collision",
    "triggered": true,
    "features": {
      "ego_x": 586203.3196629978,
      "ego_y": 4141042.828542672,
      "ego_theta": 1.3203227717536263,
      "ego_speed": 8.354161142166634,
      "obs_x": 586204.052711617,
      "obs_y": 4141045.319522671,
      "obs_type": "VEHICLE",
      "obs_theta": 1.3120518661887561,
      "obs_length": 4.933,
      "obs_width": 2.11,
      "collision_type": "front"
    }
  }
]

```

Each violation is serialized via `asdict()` from the oracle result object.

---

## Development

Linting and formatting:

```bash
ruff check .
ruff format .
```

Entry point:

```
apollo_oracle.cli:main
```
