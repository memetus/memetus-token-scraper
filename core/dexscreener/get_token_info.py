import requests
import sys
from utils.error.argv_error import handle_argv_error
from utils.error.request_error import handle_request_error

def get_recent_token():
  try:
    response = requests.get(
      "https://api.dexscreener.com/token-profiles/latest/v1",
      headers={},
    )
    data = response.json()
    print(data)

  except requests.exceptions.RequestException as e:
    handle_request_error(e, [])


def get_boost_latest_token():
  try:
    response = requests.get(
      "https://api.dexscreener.com/token-boosts/latest/v1",
      headers={},
    )
    data = response.json()
    print(data)

  except requests.exceptions.RequestException as e:
    handle_request_error(e, [])

def get_boost_top_token():
  try:
    response = requests.get(
      "https://api.dexscreener.com/token-boosts/top/v1",
      headers={},
    )
    data = response.json()
    print(data)

  except requests.exceptions.RequestException as e:
    handle_request_error(e, [])

def get_token_by_address(address: str):
  try:
    response = requests.get(
      f"https://api.dexscreener.com/latest/dex/tokens/{address}",
      headers={},
    )
    data = response.json()
    print(data)
  except requests.exceptions.RequestException as e:
    handle_request_error(e, [])

def get_token_by_keyword(keyword: str):
  try:
    response = requests.get(
      f"https://api.dexscreener.com/latest/dex/search?q={keyword}",
      headers={},
    )
    result = []
    data = response.json()

    for token in data.get('pairs'):
      if token.get('chainId') == 'solana':
        result.append(token)

    print(result)
  except requests.exceptions.RequestException as e:
    handle_request_error(e, [])

def main(argv):
  if (len(argv) < 2):
    handle_argv_error(1, [])

  if (argv[1] == "get_recent_token"):
    get_recent_token()
  elif (argv[1] == "get_boost_latest_token"):
    get_boost_latest_token()
  elif (argv[1] == "get_boost_top_token"):
    get_boost_top_token()
  elif (argv[1] == "get_token_by_address"):
    if (len(argv) < 3):
      handle_argv_error(1, [])
    elif (len(argv) > 3):
      handle_argv_error(2, [])
    get_token_by_address(argv[2])
  elif (argv[1] == "get_token_by_keyword"):
    if (len(argv) < 3):
      handle_argv_error(1, [])
    elif (len(argv) > 3):
      handle_argv_error(2, [])
    get_token_by_keyword(argv[2])
    
if __name__ == "__main__":
  main(sys.argv)
