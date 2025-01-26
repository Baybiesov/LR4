# TODO решите задачу

#def task() -> float:


#print(task())

import json


def task() -> float:

    json_file_path = 'input.json'
    total_sum = 0.0

    with open(json_file_path, 'r') as file:
        data = json.load(file)

        for entry in data:
            if 'score' in entry and 'weight' in entry:
                total_sum += entry['score'] * entry['weight']

    return round(total_sum, 3)


print(task())





