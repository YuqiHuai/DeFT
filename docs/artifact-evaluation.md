## Artifact Evaluation Guide

This section explains how to reproduce the quantitative results
reported in Section 5 of the paper.

All experimental results are provided under the `experiments/` directory,
organized by research question (RQ).

```
experiments/
  raw_data/
  rq1_process.py
  rq2_process.py
  rq3_process.py
```

> **Note on Raw Scenario Data Availability**
>
> The original experiment involved large-scale scenario
> generation and repeated system-level executions across thousands of
> scenarios. These runs produced terabytes of simulation recodings.
>
> Due to storage and distribution limitations, it is not feasible to host
> the complete raw simulation dataset.
>
> Instead, we provide the processed measurement data necessary to
> reproduce all quantitative results reported in the paper.
>
> The provided scripts deterministically regenerate the tables and metrics
> from Section 5 without requiring re-execution of Baidu Apollo.
>
> Researchers who wish to regenerate the raw data may follow the full
> experimental pipeline described in the paper and in this README.

---

### Reproducing RQ1 — Planning Reproducibility

Navigate to:

```bash
cd experiments
```

Run:

```bash
poetry run python rq1_process.py
```

This script:

- Loads planning trajectory distance measurements
- Computes reproduction counts under different thresholds
- Prints results corresponding to Table X in the paper

Expected output includes:

- `processed_data/rq1_violations.csv` (Table 1), which summarizes the number
  of generated scenarios and detected collision scenarios across the
  scenario generators.

- `processed_data/rq1_similarity.csv` (Table 2), which reports planning
  trajectory similarity measurements under different simulation outcomes.

- `processed_data/rq1_reproduce.csv` (Table 3), which records the number of
  successfully reproduced planning executions and quantifies the improvement
  achieved by DeFT over traditional system-level reruns.

---

### Reproducing RQ2 — Failure Reproducibility

Navigate to:

```bash
cd experiments
```

Run:

```bash
poetry run python rq2_process.py
```

This script:

- Loads rerun results across 10 executions
- Computes deterministic failure reproduction rate
- Compares system-level tests and DeFT module tests

Expected output includes:


- `processed_data/rq2_reproduce.csv` (data for Figure 7), which summarizes
  failure reproduction results across 10 reruns, including the number of
  reproducible failures for system-level scenario tests and for DeFT
  module tests.

---

### Reproducing RQ3 — Efficiency

Navigate to:

```bash
cd experiments
```

Run:

```bash
poetry run python rq3_process.py
```

This script:

- Computes average extraction time
- Computes average module execution time
- Computes Time-To-Reproduce-Failure (TTRF)
- Reports reduction percentage (43.69%–77.64%)

Expected outputs include:

- `rq3_efficiency.csv` (Table 5), which summarizes the runtime cost
  comparison between system-level reruns and DeFT.

- `rq3_ttr.csv` (Table 6), which reports the Time-To-Reproduce-Failure (TTRF)
  for failing scenarios and quantifies the percentage reduction achieved
  by DeFT compared to system-level reruns.