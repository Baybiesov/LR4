# TODO импортировать необходимые молули


#INPUT_FILENAME = "input.csv"
# ...  # TODO Сериализовать в файл с отступами равными 4


#if __name__ == '__main__':
    # Нужно для проверки
   # task()

   # with open(OUTPUT_FILENAME) as output_f:
    #    for line in output_f:
    #        print(line, end="")

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:

    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csvfile:

        reader = csv.DictReader(csvfile)
        json_data = [row for row in reader]


    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")