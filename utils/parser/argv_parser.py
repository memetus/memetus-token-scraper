from typing import List, Tuple
from typing_extensions import TypedDict

from utils.error.argv_error import handle_argv_error
from utils.parser.url_parser import is_valid_url

class Argument(TypedDict):
  type: str
  target_url: str


def parse_argv(argv: List[str]) -> Tuple[str, str]:
  type_index = argv.index('--type')
  url_index = -1
  
  for index, value  in enumerate(argv):
    if  "https://" in value:
      url_index = index
      break

  if url_index == -1:
    handle_argv_error(4, [])
  elif is_valid_url(argv[url_index]) == False:
    handle_argv_error(5, [])
  elif type_index == -1 or type_index == len(argv) - 1:
    handle_argv_error(3, [])
  elif argv[type_index + 1] not in ['common', 'cron']:
    handle_argv_error(6, [])

  type = argv[type_index + 1]
  target_url = argv[url_index]  
  return [type, target_url]