# DeFT: Maintaining Determinism and Extracting Unit Tests for Autonomous Driving Planning

[![ICSE 2026 Research Track](https://img.shields.io/badge/ICSE%202026-Research%20Track-blue?style=flat-square)](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/210/DeFT-Maintaining-Determinism-and-Extracting-Unit-Tests-for-Autonomous-Driving-Planni)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.1145%2F3744916.3773252-blue?style=flat-square)](https://doi.org/10.1145/3744916.3773252)
[![Artifact DOI](https://img.shields.io/badge/Artifact%20DOI-10.5281%2Fzenodo.17978768-blue?style=flat-square)](https://doi.org/10.5281/zenodo.17978768)
[![Virtual Machine DOI](https://img.shields.io/badge/Virtual%20Machine%20DOI-10.5281%2Fzenodo.18615907-blue?style=flat-square)](https://doi.org/10.5281/zenodo.18615907)
[![GitHub](https://img.shields.io/badge/GitHub-YuqiHuai%2FDeFT-black?logo=github&style=flat-square)](https://github.com/YuqiHuai/DeFT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)

This repository corresponds to the ICSE 2026 Research Track paper and its accompanying artifact, DeFT, a methodology that complements scenario-based testing by turning non-deterministic system-level scenario-based test executions into deterministic module-level frame-based tests, enabling precise reproduction of executions and failures observed in realistic simulations. For more details, see the [camera-ready paper](publication/ICSE_2026_DeFT.pdf) and the accompanying [presentation](publication/1645_Huai_DeFT.pdf).

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Quick Start: Try DeFT on Sample Scenario](#quick-start-try-deft-on-sample-scenario)
- [Artifact Evaluation](#artifact-evaluation)
- [Reproducing Experimental Results](#reproducing-experimental-results)

---

## Prerequisites

To run **DeFT** and reproduce the experimental results, the following environment is required.

### Hardware
- **CPU:** 8-core processor (minimum)
- **Memory:** 16 GB RAM (minimum)
- **GPU (strongly recommended):**
  - NVIDIA **Turing** or newer

### Operating System
- **Ubuntu:** 18.04, 20.04, or 22.04

### GPU Drivers
- **NVIDIA:** Driver version **520.61.05** or newer  

### Containerization
- **Docker-CE:** version **19.03** or newer
- **NVIDIA Container Toolkit** (for GPU acceleration inside Docker)

### Python Environment
- **uv** (dependency management and virtual environments)

---

## Project Structure

### `apollo_modules/`

This directory contains compiled protobuf files for DeFT's python implementation.

### `apollo_oracle/`

This directory contains the Python-based scenario analysis framework, including
the CLI entrypoint, oracle extension system, map and vehicle parameter utilities,
and core logic for analyzing Baidu Apollo record files. See additional documentation in [`apollo_oracle/README.md`](apollo_oracle/README.md).

### `apollo_resim/`

This directory contains the Python-based re-simulation framework for Baidu Apollo.
It provides a CLI entrypoint and core logic for launching an Apollo Docker
container, replaying an input record, and generating a re-simulated output
record using a specified HD map. See additional documentation in [`apollo_resim/README.md`](apollo_resim/README.md).

> If you plan to run re-simulation, you must perform a full Apollo installation.
> Run:
>
> ```bash
> bash scripts/install_apollo.sh --full
> ```
>
> The minimal installation is insufficient for re-simulation because
> required modules will not be built.


### `cpp/`

This directory contains parts of DeFT that are implemented in C++. Additional documentation
can be found under `cpp/README.md`. This portion of DeFT focuses on loading and execution module
tests, as well as using appropriate Bazel functionality to obtian code coverage report for the
module tests.

### `deft/`

This directory contains parts of DeFT that are implemented in Python. More specifically, this
portion of DeFT focuses on loading scenario record files, identifying inputs and outputs of the planning
module, write extracted module tests to files, and running relevant scripts to execute module tests.

#### Implementation Variants

This repository includes multiple implementations of DeFT that reflect different tradeoffs between
generality, efficiency, and required inputs.

The DeFT methodology described in the paper reconstructs planning module inputs from system-level
executions without requiring internal instrumentation. Implementations may use metadata already
published by a target ADS to reduce the candidate search. Such metadata is an optimization: generic
TISE can reconstruct an output-reproducing frame without it, although identifying the exact historical
frame may require more search.

- **DeFTLast (baseline)**  
  A heuristic-based implementation that reconstructs planning inputs using message timestamps and
  the "latest-before-time" strategy. This metadata-free baseline is a simpler approximation of TISE.
  This is the initial implementation of DeFT and in practice we observe input frames reconstructed
  by this baseline approach leads to many unexpected Apollo planning module errors due to incorrect
  frame construction time.

- **DeFTLog (ground-truth reader)**
  An evaluation utility that reads instrumented `msg.deft.*` fields containing the actual input identifiers
  observed during execution. These fields are used only as ground truth for validating planner determinism;
  they are not consumed by `DeFTApollo` and are not required by DeFT.

- **DeFTHeuristic (TISE-based)**  
  A heuristic-based implementation that reconstructs planning inputs using Time-Sensitive Input Search (TISE). 
  This variant estimates frame creation times and selects input messages based on temporal proximity and 
  consistency heuristics. It does not rely on system-specific metadata and represents the metadata-free
  realization of the DeFT methodology that produced deterministic module tests.

- **DeFTApollo (Apollo-optimized)**  
  The implementation used by the default CLI. It uses metadata present in Apollo planning outputs
  to infer the frame creation time and identify the routing, chassis, localization, and prediction
  messages. Since the metadata does not expose every required identifier, this implementation applies TISE to
  reconstruct traffic-light messages. The metadata reduces search cost and ambiguity but is not required for
  reconstruction correctness.

### `plot_frame`

This directory contains utility feature to plot a frame for illustration purpose.

### `data/`

This directory contains HD maps that are necessary for Apollo and a sample scenario to verify
the functionality of this implementation of DeFT.

### `scripts/`

This directory contains helper scripts for installing and configuring
Apollo and related dependencies used by DeFT.

#### `install_apollo.sh`

Installs and builds Baidu Apollo inside Docker.

- Clones the Apollo repository (if not already cloned)
- Starts the development container
- Builds Apollo

By default, a minimal build is performed.  
To perform a full installation (required for re-simulation):

```bash
bash scripts/install_apollo.sh --full
```

#### `install_hd_maps.sh`

Installs HD map data into the expected project structure.

- Copies map data into `apollo/modules/map/data`
- Ensures Apollo can access installed maps

Use this when setting up new map datasets.

#### `set_hd_map.sh`

Sets the active HD map used by Apollo.

- Updates `global_flagfile.txt`
- Configures `--map_dir` for Apollo (replacing any previously configured map)

Example:

```bash
bash scripts/set_hd_map.sh sunnyvale_loop
```

Use this before running Apollo or oracle analysis to ensure
the correct map is selected. `deft execute` performs the same configuration
automatically using the map detected from the record, so this script is only
needed for workflows that do not go through the DeFT CLI.

### `examples/deft_autoware`

To demonstrate the generalizability of frame-based testing beyond Apollo, we developed a variant of DeFT for Autoware. However, due to Autoware’s rapid and continuous evolution, keeping this implementation up to date and reliably reproducible is challenging. This variant uses `rclpy` to implement a subscriber node that records message interactions during scenario simulation, along with a test publisher node that feeds these messages back to the planning module. This approach, recommended during an Autoware planning working group meeting, achieves the same level of determinism.

---

## Quick Start: Try DeFT on Sample Scenario

0. Enter the directory by running

    ```bash
    cd DeFT
    ```

1. Install Apollo using the provided script.

    ```bash
    bash scripts/install_apollo.sh
    ```

2. Install Apollo HD Maps

    ```bash
    bash scripts/install_hd_maps.sh
    ```

3. *(Optional)* Specify HD Map to be used by Apollo

    ```bash
    bash scripts/set_hd_map.sh sunnyvale_loop
    ```

    > This step is optional: `deft extract` detects the HD map from the record and
    > `deft execute` configures Apollo accordingly. Run this only to pin a map
    > explicitly, or when using Apollo outside of the DeFT CLI.

4. Install DeFT's dependencies

    ```bash
    uv sync
    ```

5. Run DeFT's main algorithm to extract module tests

    ```bash
    uv run deft extract data/test_scenario_1.00000
    ```

    > The HD map used by the record is detected and recorded in
    > `out/testdata/deft_meta.json`. Pass `--map <name>` to override it.

    > By default, module tests will be stored under `out/testdata`. These module tests
    > represent input and expected output pairs for the planning module in protobuf
    > binary file format.

6. Run DeFT's main algorithm to execute module tests

    ```bash
    uv run deft execute
    ```

    > Apollo is first configured with the HD map recorded during extraction
    > (`--map <name>` overrides it, `--no-set-map` leaves the current configuration
    > untouched). Module tests extracted from the previous step under `out/testdata` are loaded into 
    > DeFT-Apollo container and executed using an dedicated module test execution entry 
    > point. After processing, all actual outputs of the planning module are
    > stored under `out/testdata_out/{test_index}/deft.bin`.

7. Run validation script to verify accuracy of reproduced planning trajectories

    ```bash
    uv run deft validate
    ```

    > This script also converts `deft.bin` (actual planning module output) and `planning.bin`
    > (expected planning module output) into ASCII format for readability purposes.

    The expected output of the script is

    ```text
    Total reproduced trajectories: 305
    Min reproduce error: 0.0
    Max reproduce error: 4.560464412474593e-05
    Avg reproduce error: 1.49607024122015e-07
    ```

    Which indicates DeFT successfully reproduced the 305 planning module outputs that were recorded in the sample scenario with a maximum error of 4.560464412474593e-05 and an average error of 1.49607024122015e-07.

    Repeated execution of the above steps produces identical outputs, demonstrating the deterministic nature of the extracted module tests.

---

## Artifact Evaluation

See [docs/artifact-evaluation.md](docs/artifact-evaluation.md)

---

## Reproducing Experimental Results

See [docs/reproducing-experiments.md](docs/reproducing-experiments.md)
