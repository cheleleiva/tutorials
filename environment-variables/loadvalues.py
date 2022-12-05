from dotenv import dotenv_values
import json

config = dotenv_values()
print(json.dumps(config))