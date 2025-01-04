import sys
import csv
import json
from typing import List

def format_csv_to_json(input_files: List[str]) -> None:
  for input_file in input_files:
    output_file = input_file.replace('.csv', '.json')
    with open(input_file, 'r', encoding='utf-8') as csv_file:
      csv_reader = csv.reader(csv_file)

      headers = next(csv_reader)

      json_data = []
      for row in csv_reader:
        json_data.append({headers[i]: row[i] for i in range(len(headers))})

      with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
  argv = sys.argv[1:]
  format_csv_to_json(argv)
