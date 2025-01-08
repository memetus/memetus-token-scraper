from tavily import TavilyClient
import os 
import json
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def get_serp_result():
  input_file = ''

  tool = [
    Tool(
      name="serp-search",
      func=serp_client.run,
      description="Useful for answering questions about current events or retrieving data from Google Search."
    )
  ]

  with open(input_file, 'r', encoding="utf-8") as file:
    datas = json.load(file)
    tokens = []
    descs = []

    for data in datas:
      print(data.get('name'), 'is processing')
      type_str = ", ".join(data.get('types'))
      
      query = f""""""
      llm = OpenAI(temperature=0)
      agent = initialize_agent(tool, llm, agent="zero-shot-react-description", verbose=True)
      res = agent.run(query)
      descs.append(res)
    
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


def get_tavily_by_address():
  input_file = ''

  with open(input_file, 'r', encoding="utf-8") as file:
    datas = json.load(file)
    tokens = []

    for data in datas:
      print(data.get('name'), 'is processing')
      type_str = ", ".join(data.get('types'))
      query = f''
      response = tavily_client.search(query=query)
      ress = response['results']
      descs = []

      for res in ress:
        descs.append(f"###title\n{res['title']}\n###content{res['content']}")
      
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
