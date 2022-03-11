import requests
import os
import dotenv

dotenv.load_dotenv()

app_id = os.environ.get('OXFORD_DICT_ID')
app_key = os.environ.get('OXFORD_DICT_KEY')

word = 'Car'
url = f'https://od-api.oxforddictionaries.com:443/api/v2/entries/en-us/{word.lower()}'

headers = { 'app_id': app_id, 'app_key': app_key }
response = requests.get(url, headers = headers)

print(f'{word}:', response.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
