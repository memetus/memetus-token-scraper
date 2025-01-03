import tweepy
import os
import sys
from dotenv import load_dotenv
from utils.error.argv_error import handle_twitter_argv_error
from utils.error.tweepy_error import handle_tweepy_error 

load_dotenv()

os.environ['TWITTER_AUTH_TOKEN'] = os.getenv('TWITTER_AUTH_TOKEN')

TWITTER_AUTH_TOKEN = os.environ['TWITTER_AUTH_TOKEN']

client = tweepy.Client(bearer_token=TWITTER_AUTH_TOKEN)

def get_search_token(keyword: str, count=100):
  try: 
    response = client.search_recent_tweets(
      query=keyword,
      max_results=count,
      tweet_fields=["created_at", "author_id", "text"],
      expansions="author_id"
    )

    return response

  except tweepy.TweepError as e:
    handle_tweepy_error(e, False)

def main(argv):
  if (len(argv) < 3):
    handle_twitter_argv_error(1, [])
  elif (len(argv) > 3):
    handle_twitter_argv_error(2, [])

  result = get_search_token(argv[1], int(argv[2]))
  print(result)

if __name__ == "__main__":
  main(sys.argv)