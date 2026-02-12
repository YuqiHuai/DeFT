import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

latex = {
    'scenorita': '\\scenorita',
    'deeepcollision': '\\deepcollision',
    'doppeltest': '\\doppeltest',
    'behavexplor': '\\behavexplor',
    'avfuzzer': '\\avfuzzer',
    'drivefuzzer': '\\drivefuzz',
    'samota': '\\samota',
    'decictor': '\\decictor'
}

labels = {
    'scenorita': 'scenoRITA',
    'deeepcollision': 'DeepCollision',
    'doppeltest': 'DoppelTest',
    'behavexplor': 'BehAVExplor',
    'avfuzzer': 'AV-FUZZER',
    'drivefuzzer': 'DriveFuzz',
    'samota': 'SAMOTA',
    'decictor': 'Decictor'
}

violation_counter = defaultdict(lambda: defaultdict(lambda: 0))

reproduced_similarities = []
unreproduced_similarities = []

threshold_values = sorted(
    [0.0, 0.1, 0.23, 1.62, 6.99, 17.15, 29.56, 139.51, 308.71, 1453.07, 2320.81]
)

reproduce_counter = defaultdict(lambda: defaultdict(lambda: 0))

for scenario_filename in Path("raw_data/oracle").iterdir():
    elements = scenario_filename.name.split(".")[0].split("_")
    approach = elements[0]
    scenario_id = f"{elements[1]}_{elements[2]}"
    with open(scenario_filename, 'r') as fp:
        data = json.load(fp)

    initial_violation = data['initial_violation']
    subsequent_violation = data['subsequent_violation']
    subsequent_comparison = data['subsequent_comparison']
    deft_comparison = data['deft']

    subsequent_deft = data['subsequent_deft']

    if 'collision' in initial_violation:
        violation_counter[latex[approach]]['collision'] += 1

        if all('collision' in sv for sv in subsequent_violation):
            violation_counter[latex[approach]]['deterministic'] += 1
        else:
            violation_counter[latex[approach]]['non_deterministic'] += 1

        counter = 0
        for sv, sc, sd in zip(subsequent_violation, subsequent_comparison, subsequent_deft):
            counter += 1
            if len(sc) != len(deft_comparison):
                diff = len(sc) - len(deft_comparison)
                sc = sc[diff:]

            if 'collision' in sv:
                reproduced_similarities.extend(sc[1:])
            else:
                unreproduced_similarities.extend(sc[1:])

            for theta in threshold_values:
                reproduce_counter[theta][f'DeFT_{counter}'] += len([x for x in sd[1:] if x <= theta])
                reproduce_counter[theta][f'S_{counter}'] += len([x for x in sc[1:] if x <= theta])

                if counter > 1:
                    # check for non-determinism
                    assert reproduce_counter[theta][f'DeFT_{counter}'] == reproduce_counter[theta][f'DeFT_{counter-1}']
    else:
        violation_counter[latex[approach]]['no_collision'] += 1



df = pd.DataFrame.from_dict(violation_counter, orient='index')
df = df.reindex(columns=['no_collision', 'collision', 'deterministic', 'non_deterministic'])
df = df.reindex(sorted(latex.values()))
df.loc['Total'] = df.sum()
df.index.name = "Approach"
df.to_csv("processed_data/rq1_violations.csv")

df = pd.DataFrame(reproduced_similarities, columns=["Values"])

# Compute required statistics
summary = pd.DataFrame({
    "FR": [
        np.min(reproduced_similarities),
        np.quantile(reproduced_similarities, 0.25),
        np.median(reproduced_similarities),
        np.quantile(reproduced_similarities, 0.75),
        np.max(reproduced_similarities),
        np.mean(reproduced_similarities)
    ],
        "FN": [
        np.min(unreproduced_similarities),
        np.quantile(unreproduced_similarities, 0.25),
        np.median(unreproduced_similarities),
        np.quantile(unreproduced_similarities, 0.75),
        np.max(unreproduced_similarities),
        np.mean(unreproduced_similarities)
    ]
}, index=["min", "Q1", "median", "Q3", "max", "mean"])
summary.index.name = 'Measure'
summary.to_csv("processed_data/rq1_similarity.csv")
thresholds = set()
for t1, t2 in summary.values.tolist():
    thresholds.add(round(t1, 2))
    thresholds.add(round(t2, 2))
thresholds = sorted(list(thresholds))
print(thresholds)

reproduce_df = pd.DataFrame.from_dict(reproduce_counter, orient='index')

reproduce_df.index.name = "theta"
reproduce_df.to_csv("processed_data/rq1_reproduce.csv")
print(reproduce_df)
