import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.spoonacular.com/recipes/random/?'
url += 'apiKey='
url += '&number=100'

req = requests.get(url)
print(req.json())

import json
with open('recipes.json', 'w') as fp:
    json.dump(req.json(), fp)