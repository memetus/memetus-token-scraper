import os 
import json
import requests
from tavily import TavilyClient
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, ToolMessage
import time

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
os.environ["SERP_API_KEY"] = os.getenv('SERP_API_KEY')

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
SERP_API_KEY = os.environ["SERP_API_KEY"]

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def get_analysis_by_url(model_id: str):
  input_file = ''
  with open(input_file, 'r', encoding='utf-8') as file:
    datas = json.load(file)
    tokens = []

    for data in datas[152:154]:
      urls = data.get('urls', [])
      print(data.get('name'), 'is processing')
      descs = []

      for url in urls:
        if ('https://x.com') in url or ('https://twitter.com') in url:
          print('Twitter URL detected, skipping analysis.')
        else:
          headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
          }
          res = requests.get(url, headers=headers, timeout=10)
          soup = BeautifulSoup(res.content, 'html.parser')
          text = soup.get_text()
          system_message = SystemMessage(
            content=""
          )
          human_message = HumanMessage(content=text)
          llm = ChatOpenAI(model=model_id ,temperature=0)
          time.sleep(10)
          res = llm.invoke([system_message, human_message])
          descs.append(res.content)

      tokens.append({
        'name': data['name'],
        'symbol': data['symbol'],
        'address': data['address'],
        'types': data['types'],
        'urls': data['urls'],
        'descriptions': descs
      })

    output_file = input_file.replace('.json', 'output.json')
    with open(output_file, 'w', encoding='utf-8') as file:
      json.dump(tokens,
      file,
      ensure_ascii=False,
      indent=2)
