import os
from dotenv import load_dotenv

load_dotenv()


api_key_env = os.getenv('API_KEY')
print(api_key_env)
