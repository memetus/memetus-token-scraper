from typing import List

def handle_argv_error(code: int, messages: List[str]):
  if code == 1:
    print('error: missing argument')
  elif code == 2:
    print('error: too many arguments')
  elif code == 3:
    print('error: --type argument not found')
  elif code == 4:
    print('error: url not found')
  elif code == 5:
    print('error: invalid url')
  elif code == 6:
    print('error: invalid --type argument')
  print('usage: python main.py --type <type> <target_url>')
  
  for message in messages:
    print(message)
  exit(1)

def handle_twitter_argv_error(code: int, messages: List[str]):
  if code == 1:
    print('error: missing argument')
  elif code == 2:
    print('error: too many arguments')

  print('usage: python core/twitter/scrap_account.py <keyword> <count>')
  for message in messages:
    print(message)
  exit(1)

def handle_geckoterminal_argv_error(code: int, messages: List[str]):
  if code == 1:
    print('error: missing argument')
  elif code == 2:
    print('error: too many arguments')

  print('usage: python core/geckoterminal/get_scrap.py <type>')
  for message in messages:
    print(message)
  exit(1)