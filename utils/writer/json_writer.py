import json

def create_json_file(data, file_name):
  with open(file_name, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)