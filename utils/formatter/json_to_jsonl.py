import json
import sys
from typing import List

def format_json_to_jsonl(input_files: List[str]) -> None:
  for input_file in input_files:
    with open(input_file, 'r', encoding='utf-8') as infile, open('output' + input_file, 'w', encoding='utf-8') as outfile:
      data = json.load(infile)  
      for entry in data:
        json.dump(entry, outfile)  
        outfile.write("\n")  

if __name__ == "__main__":
  argv = sys.argv[1:]
  format_json_to_jsonl(argv)