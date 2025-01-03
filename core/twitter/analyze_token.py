from core.dexscreener.get_token_info import get_token_by_address
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

def get_project_tweet(project_handle: str, id: str):
  try:
    response = client.get_users_tweets(id, max_results=100)
    tweet_text_list = [tweet.text for tweet in response.data]
    return {
      'username': project_handle,
      'tweets': tweet_text_list
    }
  except tweepy.TweepError as e:
    handle_tweepy_error(e, False)


def get_project_account(address: str):
  project_handle = None
  token = get_token_by_address(address)
  socials = token.get('pairs')[0].get('info').get('socials')

  for social in socials:
    if social.get('type') == 'twitter':
        project_handle = social.get('url').split('/')[-1]
  if project_handle is None:
    return None
  try:
    response = client.get_user(username=project_handle)
    return response.data

  except tweepy.TweepError as e:
    handle_tweepy_error(e, False)

def main(argv):
  if (len(argv) < 2):
    handle_twitter_argv_error(1, [])
  elif (len(argv) > 2):
    handle_twitter_argv_error(2, [])
    
  accout_result = get_project_account(argv[1])
  tweet_result = get_project_tweet(accout_result.username, accout_result.id)

  print(tweet_result)

if __name__ == "__main__":
  main(sys.argv)
