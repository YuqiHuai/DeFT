# DeFT: Maintaining Determinism and Extracting Unit Tests for Autonomous Driving Planning

[![ICSE 2026 Research Track](https://img.shields.io/badge/ICSE%202026-Research%20Track-blue?style=flat-square)](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/210/DeFT-Maintaining-Determinism-and-Extracting-Unit-Tests-for-Autonomous-Driving-Planni)
[![Artifact DOI](https://img.shields.io/badge/Artifact%20DOI-10.5281%2Fzenodo.17978768-blue?style=flat-square)](https://doi.org/10.5281/zenodo.17978768)
[![GitHub](https://img.shields.io/badge/GitHub-YuqiHuai%2FDeFT-black?logo=github&style=flat-square)](https://github.com/YuqiHuai/DeFT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)

This repository corresponds to the ICSE 2026 Research Track paper and its accompanying artifact, **DeFT**, a tool and methodology designed to improve testing reliability in autonomous driving systems by addressing non-determinism in planning tests. Traditional system-level scenario tests often produce varying outcomes, making failure reproduction and debugging challenging. DeFT is a methodology that converts non-deterministic system-level scenario tests into deterministic module-level tests by extracting and reconstructing planning inputs.

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
- **Python Poetry** (dependency management and virtual environments)

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
- Configures `--map_dir` for Apollo

Example:

```bash
bash scripts/set_hd_map.sh sunnyvale_loop
```

Use this before running Apollo or oracle analysis to ensure
the correct map is selected.

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

3. Specify HD Map to be used by Apollo

    ```bash
    bash scripts/set_hd_map.sh sunnyvale_loop
    ```

4. Install DeFT's dependencies

    ```bash
    poetry install
    ```

5. Run DeFT's main algorithm to extract module tests

    ```bash
    poetry run deft extract data/test_scenario.00000
    ```

    > By default, module tests will be stored under `out/testdata`. These module tests
    > represent input and expected output pairs for the planning module in protobuf
    > binary file format.

6. Run DeFT's main algorithm to execute module tests

    ```bash
    poetry run deft execute
    ```

    > Module tests extracted from the previous step under `out/testdata` are loaded into 
    > DeFT-Apollo container and executed using an dedicated module test execution entry 
    > point. After processing, all actual outputs of the planning module are
    > stored under `out/testdata_out/{test_index}/planning.bin`.

7. Run validation script to verify accuracy of reproduced planning trajectories

    ```bash
    poetry run deft validate
    ```

    > This script also converts `deft.bin` (expected planning module output) and `planning.bin`
    > (actual planning module output) into ASCII format for readability purposes.

    The expected output of the script is

    ```text
    Total reproduced trajectories: 305
    Min reproduce error: 0.0
    Max reproduce error: 4.560464412474593e-05
    Avg reproduce error: 1.49607024122015e-07
    ```

    Which indicates DeFT successfully reproduced the 305 planning module outputs that were recorded in the sample scenario with a maximum error of 1.49607024122015e-07.

    Repeated execution of the above steps produces identical outputs, demonstrating the deterministic nature of the extracted module tests.

---

## Artifact Evaluation

See [docs/artifact-evaluation.md](docs/artifact-evaluation.md)

---

## Reproducing Experimental Results

See [docs/reproducing-experiments.md](docs/reproducing-experiments.md)