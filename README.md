## This is HOMO-MEMETUS Token Scrap Repository

---

This repository does not include any code or logic to AI Agent training. This repository contains code for collecting tokens and token information from Twitter, Dexscreener, and GeckoTerminal. The collected data will be stored in a database as part of the dataset used to train the Agent and as potential tradeable item options for the Agent. While it's understood that direct access to RPC endpoints or other sources like Raydium could be used to gather token information, this repository excludes those since they are implemented in TypeScript.

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
- search token by twitter account(might be KoL) post
- search token metadata by dexscreener
- scrap token chart by selenium

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
```

#### Environment Variable

```bash
TWITTER_AUTH_TOKEN
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
