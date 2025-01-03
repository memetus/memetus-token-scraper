from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
  try:
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)
  except Exception:
    return False
