# DeFT CPP Implementation Overview

This section describes the purpose and scope of each directory in this repository. All contents represent **C++ changes that are either added to or modified from Apollo v7**.

---

## `deft/`

The `deft` directory contains a **custom executable layer** built on top of Apollo v7. It provides an alternative entry point and supporting scripts for running and validating planning module tests extracted by DeFT.

This directory should be placed under `apollo/modules/`.

### Contents

- **`BUILD`**  
  Bazel build rules used to produce the `deft` executable, linking against Apollo v7
  planning dependencies.

- **`main.cc`**  
  Custom planning module entry point. Initializes Apollo planning module and executes
  the extracted module tests.

- **`deft.sh`**  
  Wrapper script used to run the custom executable in an Apollo v7 environment.

- **`coverage.sh`**  
  Script for generating code coverage reports for the planning module.

---

## `modules/`

This directory mirrors Apollo’s standard module layout and contains **only the files
that have been modified or extended**. Similar modifications can be made to other 
modules so that DeFT can be used to reproduce their executions

### Source Files

- **`planning_component.cc`**  
  Applies a [bug fix](https://github.com/ApolloAuto/apollo/commit/9c764ed81b06f6935e658122e6b5cb507fce265e) to Apollo v7’s planning module that previously produced incorrect timestamps in planning outputs. The fix ensures temporal consistency required for accurate reconstruction of input frames.

- **`on_lane_planning.cc`**  
  Slightly modifies planning module execution to record information necessary to reconstruct 
  planning input frames, avoiding unnecessary state duplication.

### Configuration
- **`planning.conf`**  
  Disables `trajectory_stitcher` and `reference_line_provider_thread`, which introduce
  unresolved non-determinism.

### Protocol Buffers
- **`planning.proto`**  
  Adds DeFT-specific protobuf messages designed to **efficiently record information regarding
  planning inputs** with minimal overhead. These messages are later used to reconstruct
  planning input frames for testing and validation.
