from typing import List

def handle_request_error(code: int, messages: List[str]):
  if 400 <= code < 500:
    print('network error: client error', code)
  elif 500 <= code < 600:
    print('network error: server error', code)
  
  for message in messages:
    print(message)
  exit(1)
