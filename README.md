## This is HOMO-MEMETUS Token Scrap Repository

---

This repository does not include any code or logic to AI Agent training. This repository contains code for collecting tokens and token information from Twitter, Dexscreener, GeckoTerminal, News scrap and Googling. The collected data will be stored in a database as part of the dataset used to train the Agent and as potential tradeable item options for the Agent. While we are understanding that direct access to RPC endpoints or other sources like Raydium could be used to gather token information, this repository excludes those since they are implemented in TypeScript.

#### Directory Structure

```text
  .
  ├── pyproject.tml / # repository metadata & dependencies
  ├── config / # declare immutable data
  ├── core
  │ ├── dexscreener / # use dexscreener standard api
  │ ├── geckoterminal / # use selenium to scrap token data & chart image
  | ├── twitter / # provide search account by address & keyword search & scrap keyword related account
  ├── selenium / # declare selenium & manage selenium instance
  ├── utils / # declare selenium & manage selenium instance
  | ├── error / # handle error utils
  | ├── formatter / # handle formatter utils
  | ├── image / # handle image utils
  | ├── logger / # handle logger utils
  | ├── writer / # handle writer utils
  | ├── parser / # handle parser utils
  └── package.json # application dependencies
```

#### Feature

- search token by twitter keyword
- search token related twitter account to train emotional analyzer
- search token by twitter account(might be KoL account or Project account) post
- search token metadata by dexscreener
- scrap token chart by selenium
- search token by news scrap and googling module

#### Requirement

> Recommend to use pyenv, poetry

```bash
python = "^3.11"
pandas = "^2.2.3"
google-search-results = "^2.4.2"
beautifulsoup4 = "^4.12.3"
uuid = "^1.30"
selenium = "^4.27.1"
seleniumbase = "^4.33.12"
tweepy = "^4.14.0"
python-dotenv = "^1.0.1"
openai = "^1.59.2"
langchain = "^0.3.13"
langchain-community = "^0.3.13"
langchainhub = "^0.1.21"
langgraph = "^0.2.60"
langsmith = "^0.2.7"
langchain-openai = "^0.2.14"
langchain-text-splitters = "^0.3.4"
langchain-cohere = "^0.3.4"
langchain-milvus = "^0.1.7"
tavily-python = "^0.5.0"
langchain-experimental = "^0.3.4"
```

#### Environment Variable

```bash
TWITTER_AUTH_TOKEN
OPENAI_API_KEY
TAVILY_API_KEY
SERP_API_KEY
```

#### Usage

installation

```bash
poetry install
```

dexscreener

```bash
python3 core.dexscreener.get_token_info <function_name>
```

geckoternimal

```bash
python3 core.geckoterminal.get_scrap <option> <token_address>

# option: 'price-text' or 'chart'
```

twitter

```bash
python3 core.twitter.analyze_token <token_address>
```

```bash
python3 core.twitter.scrap_account <search_keyword> <count>
```

```bash
python3 core.twitter.search_token <search_keyword> <count>
```
