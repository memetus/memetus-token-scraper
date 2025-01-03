import tweepy
import os
import sys
from utils.error.argv_error import handle_twitter_argv_error
from utils.error.tweepy_error import handle_tweepy_error
from dotenv import load_dotenv

load_dotenv()

os.environ['TWITTER_AUTH_TOKEN'] = os.getenv('TWITTER_AUTH_TOKEN')

TWITTER_AUTH_TOKEN = os.environ['TWITTER_AUTH_TOKEN']

client = tweepy.Client(bearer_token=TWITTER_AUTH_TOKEN)

def get_search_account(keyword: str, count=20, min_followers=10000):
  try:
    response = client.search_recent_tweets(
      query=keyword, 
      max_results=count,
      user_fields=["username", "name", "public_metrics"],
      expansions="author_id"
    )

    users = {user["id"]: user for user in response.includes["users"]}

    results = []
    for author_id, author in users.items():
      if isinstance(author, dict) and "public_metrics" in author:
        followers_count = author["public_metrics"].get("followers_count", 0)
        if followers_count >= min_followers:
          results.append({
            "id": author["id"],
            "username": author["username"],
            "name": author["name"],
            "followers_count": followers_count,
          })

    return results



  except tweepy.TweepError as e:
     handle_tweepy_error(e, False)

def main(argv):
  if (len(argv) < 3):
    handle_twitter_argv_error(1, [])
  elif (len(argv) > 3):
    handle_twitter_argv_error(2, [])

  result = get_search_account(argv[1], int(argv[2]))
  print(result)

if __name__ == "__main__":
  main(sys.argv)
