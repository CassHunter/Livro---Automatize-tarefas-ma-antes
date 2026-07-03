# grava a pagina web em um arquivo

import requests

response = requests.get('http://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()

with open('Romeo_e_Juliet.txt', 'wb') as playFile:
    for chunk in response.iter_content(100000):
        playFile.write(chunk)

