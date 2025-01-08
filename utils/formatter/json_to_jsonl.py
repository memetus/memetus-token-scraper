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

def format_json_to_jsonl_sentiment(input_files: List[str]) -> None:
  for input_file in input_files:
    output_file = input_file.replace('.json', '.jsonl')
    with open(input_file, 'r', encoding='utf-8') as infile:
      data = json.load(infile)  
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for row in data:
          json.dump({ 
            'messages': [
              { 'role': 'user', 'content': row['text']},
              { "role": 'assistant', 'content': 'The sentiment score is ' + row['score']}
            ]
          }, outfile, ensure_ascii=False)
          outfile.write("\n")

if __name__ == "__main__":
  argv = sys.argv[1:]
  format_json_to_jsonl_sentiment(argv)