import json

def parse_finetune_prompt():
  input_file = ''
  output_file = ''

  with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    datas = json.load(infile)
    for row in datas:
      name = row.get('name')
      symbol = row.get('symbol')
      address = row.get('address')
      types = ', '.join(row.get('types', []))
      urls = ', '.join(row.get('urls', []))

      for desc in row.get('descriptions'):
        json.dump({
          'messages': [
            { 'role': 'user', 'content': f''},
            { 'role': 'assistant', 'content': f"" }
          ]
        }, outfile, ensure_ascii=False)
        outfile.write("\n")  


if __name__ == '__main__':
  parse_finetune_prompt()