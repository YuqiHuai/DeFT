import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

latex = {
    "scenorita": "\\scenorita",
    "deeepcollision": "\\deepcollision",
    "doppeltest": "\\doppeltest",
    "behavexplor": "\\behavexplor",
    "avfuzzer": "\\avfuzzer",
    "drivefuzzer": "\\drivefuzz",
    "samota": "\\samota",
    "decictor": "\\decictor",
}

labels = {
    "scenorita": "scenoRITA",
    "deeepcollision": "DeepCollision",
    "doppeltest": "DoppelTest",
    "behavexplor": "BehAVExplor",
    "avfuzzer": "AV-FUZZER",
    "drivefuzzer": "DriveFuzz",
    "samota": "SAMOTA",
    "decictor": "Decictor",
}

efficiency_timings = defaultdict(lambda: defaultdict(lambda: list()))
reproduce_timer = defaultdict(lambda: defaultdict(lambda: 0))

def get_reproduce_duration(subsequent_violation, durations):
    result = 0
    reproduced = False
    for sv, d in zip(subsequent_violation, durations):
        result += d
        if "collision" in sv:
            reproduced = True
            break
    if reproduced:
        return result
    return float("inf")


for scenario_filename in Path("raw_data/oracle").iterdir():
    elements = scenario_filename.name.split(".")[0].split("_")
    approach = elements[0]
    scenario_id = f"{elements[1]}_{elements[2]}"
    with open(scenario_filename, "r") as fp:
        data = json.load(fp)

    initial_violation = data["initial_violation"]
    subsequent_violation = data["subsequent_violation"]
    subsequent_comparison = data["subsequent_comparison"]
    subsequent_durations = data["durations"]

    key = {
        "approach": approach,
        "scenario_id": scenario_id,
        "resim_id": "resim_1",
    }
    with open(
        f"raw_data/efficiency/{approach}_{scenario_id}.json", "r"
    ) as fp:
        efficiency_obj = json.load(fp)

    efficiency_timings[approach]['System Test'].append(
        data["initial_duration"]
    )
    efficiency_timings[approach]['Module Test'].append(
        efficiency_obj['execution']
    )

    if "collision" in initial_violation:
        reproduce_time = get_reproduce_duration(
            subsequent_violation, subsequent_durations
        )
        # drop ones that are never reproduced
        if reproduce_time == float('inf'):
            continue
        reproduce_timer["System Test"][f"{approach}_{scenario_id}"] = reproduce_time
        deft_time = efficiency_obj["execution"]
        reproduce_timer["Module Test"][f"{approach}_{scenario_id}"] = deft_time

efficiency_counter = dict()
for k in efficiency_timings:
    efficiency_counter[latex[k]] = dict()
    for category in efficiency_timings[k]:
        efficiency_counter[latex[k]][category] = np.mean(
            efficiency_timings[k][category]
        )

df = pd.DataFrame.from_dict(efficiency_counter, orient='index')
df.index.name = 'Approach'
df = df.reindex(sorted(latex.values()))
df['Reduction'] = (df['System Test'] - df['Module Test']) / df['System Test'] *100
df = df.round(2)
df.to_csv("processed_data/rq3_efficiency.csv")
print('Run-time Cost Comparison')
print(df)

df = pd.DataFrame.from_dict(reproduce_timer)
ttr_values = defaultdict(lambda: defaultdict(lambda: list()))
for scenario_id, row in df.iterrows():
    elements = scenario_id.split("_")
    approach = elements[0]

    system_ttr = row['System Test']
    deft_ttr = row['Module Test']

    ttr_values[approach]['System Test'].append(system_ttr)
    ttr_values[approach]['Module Test'].append(deft_ttr)

ttr_summary = defaultdict(lambda: defaultdict(lambda: 0))

for k in ttr_values:
    for category in ttr_values[k]:
        ttr_summary[latex[k]][category] = np.mean(
            ttr_values[k][category]
        )

df = pd.DataFrame.from_dict(ttr_summary, orient='index')
df = df.reindex(sorted(latex.values()))
df['Reduction'] = (df['System Test'] - df['Module Test']) / df['System Test'] *100
df.index.name = 'Approach'
df = df.round(2)
df.to_csv("processed_data/rq3_ttr.csv")
print('TTRF Comparison')
print(df)
