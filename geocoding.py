import requests
from pprint import pprint
from config import API_KEY

url_geo = "https://api.openweathermap.org/geo/1.0/direct"

cidade = 'itapeva, SP, BR'

params = {
    'q':cidade,
    'limit':5,
    'appid': API_KEY
}

response = requests.get(url_geo, params=params)
response.raise_for_status() 

resultado = response.json()

pprint(resultado)
# [{'country': 'BR',
#   'lat': -23.9849105,
#   'local_names': {'pt': 'Itapeva', 'ru': 'Итапева'},
#   'lon': -48.8803886,
#   'name': 'Itapeva',
#   'state': 'São Paulo'}]