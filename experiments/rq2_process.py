import json
from collections import defaultdict
from pathlib import Path

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

reproduce_counter = defaultdict(lambda: defaultdict(lambda: 0))
scenarios = set()

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
    subsequent_deft_violations = data['subsequent_deft_violations']

    if 'collision' in initial_violation:
        for index, (sv, sd) in enumerate(zip(subsequent_violation, subsequent_deft_violations)):
            if 'collision' in sv:
                reproduce_counter['scenario'][index+1] += 1
            if sd:
                reproduce_counter['deft'][index+1] += 1

        if all('collision' in sv for sv in subsequent_violation):
            reproduce_counter['scenario']['A'] += 1

        if all(x for x in subsequent_deft_violations):
            reproduce_counter['deft']['A'] += 1

df = pd.DataFrame.from_dict(reproduce_counter, orient='index')
df.index.name = 'Test Type'
print(df)
df.to_csv("processed_data/rq2_reproduce.csv")
