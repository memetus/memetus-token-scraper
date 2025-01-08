import json
from core.dexscreener.get_token_info import get_token_by_address

def main():
  input_file = 'path'
  with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)
    tokens = []

    for d in data:
      token = get_token_by_address(d.get('address'))
      print(token, 'is processing')
      token_data = token.get('pairs', [])[0]

      urls = []
      urls.append(token_data.get('url'))
      for website in token_data.get('info').get('websites'):
        urls.append(website.get('url'))
      for social in token_data.get('info').get('socials'):
        urls.append(social.get('url'))

      tokens.append({
        'name': d['name'],
        'symbol': d['symbol'],
        'address': d['address'],
        'types': d['type'],
        'urls': urls
      })

    output_file = input_file.replace('.json', 'output.json')
    with open(output_file, 'w', encoding='utf-8') as file:
      json.dump(tokens,
      file,
      ensure_ascii=False,
      indent=2)

if __name__ == "__main__":
  main()