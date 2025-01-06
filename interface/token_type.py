from typing_extensions import TypedDict
from typing import List
from interface.opinion_type import Opinion

class Token(TypedDict):
  market_caps: float
  holders: int
  top_holder_ratio: float
  volumes: List[float] = []
  liquidity: float
  creator_hold: List[float] = []
  top_lp_concentration_ratio: List[float] = []
  price: float
  twitter_follower: List[int] = []
  twitter_followers_growth: float = 0.0
  twitter_mention_count: List[int] = []
  twitter_mention_growth: float = 0.0
  twitter_ticker_mention_count: List[int] = []
  twitter_ticker_mention_growth: float = 0.0
  twitter_address_mention_count: List[int] = []
  twitter_address_mention_growth: float = 0.0
  github_analysis: str = ""
  website: str = ""
  whitepaper: str = ""
  twitter: str = ""
  discord: str = ""
  telegram: str = ""
  google_search: str = ""
  news: str = ""
  rug_score: List[int] = []
  rug_score_growth: float = 0.0
  sentiment_score: List[int] = []
  sentiment_score_growth: float = 0.0
  opinions: List[Opinion] = []

def create_token() -> Token:
  return Token(
    market_caps=0.0,
    holders=0,
    top_holder_ratio=0.0,
    volumes=[],
    liquidity=0.0,
    creator_hold=[],
    top_lp_concentration_ratio=[],
    price=[],
    twitter_follower=[],
    twitter_followers_growth=0.0,
    twitter_mention_count=[],
    twitter_mention_growth=0.0,
    twitter_ticker_mention_count=[],
    twitter_ticker_mention_growth=0.0,
    twitter_address_mention_count=[],
    twitter_address_mention_growth=0.0,
    github_analysis="",
    website="",
    whitepaper="",
    twitter="",
    discord="",
    telegram="",
    google_search="",
    news="",
    rug_score=[],
    rug_score_growth=0.0,
    sentiment_score=[],
    sentiment_score_growth=0.0,
    opinions=[]
)