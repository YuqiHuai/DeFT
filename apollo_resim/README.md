# apollo_resim

Baidu Apollo record re-simulation CLI tool.

`apollo_resim` replays a Baidu Apollo record inside an docker container,
re-simulates the scenario using a specified HD map, and produces a new
record file as output.

This tool is designed for automated scenario re-execution and testing.

---

## Installation

### Requirements

- Python ≥ 3.10
- Poetry
- Docker
- Apollo 7.0

Install dependencies:

```bash
poetry install
```

---

## Usage

Run using Poetry:

```bash
poetry run apollo_resim <src_record> <dst_record> [-m <map_name>]
```

When `-m/--map` is omitted, the HD map is detected from the source record's
routing response.

Either way, Apollo's `--map_dir` is configured with the selected map before the
container is started, and the map is copied into `apollo-7.0.0/modules/map/data`
if it is not installed yet.

---

## Example

```bash
poetry run apollo_resim \
  data/test_scenario.00000 \
  resim_output.00000 \
  -m sunnyvale_loop
```

---

## Arguments

| Argument      | Description |
|--------------|------------|
| `src_record` | Path to the source Apollo record file |
| `dst_record` | Output path for the re-simulated record file (must not exist) |

---

## Options

| Option | Description |
|--------|------------|
| `-m, --map` | Map name under `data/maps/<map_name>`. Detected from the source record when omitted. |

Example expected directory layout:

```
data/
└── maps/
    └── sunnyvale_loop/
    └── borregas_ave/
```

---

## Output

The tool generates a new Apollo record file at the specified destination:

```
resim_output.00000
```

This file contains the replayed and re-simulated scenario.

---

## Internal Workflow

`apollo_resim` internally calls:

```
apollo_resim.re_simulate(...)
```

Which:

- Configures Apollo's HD map (`--map_dir`)
- Starts an Apollo Docker container
- Launches Dreamview
- Initializes simulation control
- Replays the input record
- Records the output
- Stops and cleans up the container

---

## Development

Lint and format:

```bash
ruff check .
ruff format .
```

Poetry entry point:

```
apollo_resim.cli:main
```

---

## Notes

- Requires Docker access.
- Requires working Apollo installation.
- Container is automatically cleaned up after execution.
- Designed for automation and batch scenario testing.
