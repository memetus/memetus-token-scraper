def handle_tweepy_error(exception: Exception, is_return: bool) -> None | Exception:
  print("error: ", exception)

  if is_return:
    return exception
  exit(1)
  