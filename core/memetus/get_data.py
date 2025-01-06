import os
from dotenv import load_dotenv  

load_dotenv()

os.environ['BASE_API_URL'] = os.getenv('BASE_API_URL')
os.environ['BASE_API_KEY'] = os.getenv('BASE_API_KEY')

BASE_API_KEY = os.environ['BASE_API_KEY']
BASE_API_URL = os.environ['BASE_API_URL']

print(BASE_API_KEY)
print(BASE_API_URL)