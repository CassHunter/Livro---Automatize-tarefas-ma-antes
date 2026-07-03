import sys
from datetime import datetime
import requests
from config import API_KEY

def buscar_coordenadas(cidade):
    '''Retorna as inf geográficas de uma cidade usando a 
       API Geocoding da OpenWeather.'''
    
    url_geo = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q':cidade,
        'limit':1,
        'appid': API_KEY
        }
    try:
        response = requests.get(url_geo, params=params, timeout=10)
        response.raise_for_status()
        resultado = response.json()
        if not resultado:
            print('Cidade não encontrada.')
            sys.exit()
            
        cidade_info = resultado[0]   # dicionário inteiro
        return cidade_info
    
    except requests.RequestException as erro:
        print(f'Erro: {erro}')
        sys.exit()

def buscar_clima(lat, lon):
    '''Retorna as inf climáticas de uma cidade usando a 
       API Current Weather da OpenWeather.'''
    
    url_weather = "https://api.openweathermap.org/data/2.5/weather"

    params = {
    'lat': lat,
    'lon': lon,
    'appid': API_KEY,
    'units': 'metric',
    'lang':'pt_br'
    }
    try:
        response = requests.get(url_weather, params=params, timeout=10)
        response.raise_for_status()

        dados = response.json()
        clima = {
            "temperatura": dados["main"]["temp"],
            "sensacao": dados["main"]["feels_like"],
            "temperatura_min": dados["main"]["temp_min"],
            "temperatura_max": dados["main"]["temp_max"],
            "umidade": dados["main"]["humidity"],
            "pressao": dados["main"]["pressure"],

            "descricao": dados["weather"][0]["description"].capitalize(),
            "condicao": dados["weather"][0]["main"],

            "vento": dados["wind"]["speed"],
            "direcao_vento": dados["wind"].get("deg"),

            "nuvens": dados["clouds"]["all"],
            "visibilidade": dados["visibility"] / 1000,

            "nascer_sol": datetime.fromtimestamp(dados["sys"]["sunrise"]),
            "por_do_sol": datetime.fromtimestamp(dados["sys"]["sunset"])
        }
        return clima  
    
    except requests.RequestException as erro:
        print(f'Erro: {erro}')
        sys.exit()
        
def exibir_clima(cidade_info, clima):
    '''Exibir os dados climáticos formatados'''
   
    print('=' * 40)
    print('        PREVISÃO DO TEMPO')
    print('=' * 40)

    print(f'Cidade       : {cidade_info['name']}/{cidade_info['state']} - {cidade_info['country']}')
    print(f'Condição     : {clima['descricao']}')
    print(f'Temperatura  : {clima["temperatura"]:.1f} °C')
    print(f'Sensação     : {clima["sensacao"]:.1f} °C')
    print(f'Umidade      : {clima["umidade"]}%')
    print(f'Vento        : {clima["vento"]:.1f} m/s')
    print(f'Nuvens       : {clima["nuvens"]}%')
    print(f'Visibilidade : {clima["visibilidade"]:.1f} km')
    print(f'Nascer do sol: {clima['nascer_sol'].strftime('%H:%M')}')
    print(f'Pôr do sol   : {clima['por_do_sol'].strftime('%H:%M')}')

    print('=' * 40)

def main():
    if len(sys.argv) < 2:
        print('Uso:')
        print('py weather.py cidade')
        sys.exit()
    
    cidade = ' '.join(sys.argv[1:])
    cidade_info = buscar_coordenadas(cidade)

    dados = buscar_clima(cidade_info['lat'], cidade_info['lon'])

    exibir_clima(cidade_info, dados)

if __name__ =='__main__':
    main()






# resposta API
# pprint(dados)

# {'base': 'stations',
#  'clouds': {'all': 0},
#  'cod': 200,
#  'coord': {'lat': -23.9822, 'lon': -48.8756},
#  'dt': 1783011162,
#  'id': 3460723,
#  'main': {'feels_like': 25.9,
#           'grnd_level': 936,
#           'humidity': 53,
#           'pressure': 1019,
#           'sea_level': 1019,
#           'temp': 25.87,
#           'temp_max': 25.87,
#           'temp_min': 25.87},
#  'name': 'Itapeva',
#  'sys': {'country': 'BR', 'sunrise': 1782986338, 'sunset': 1783024787},
#  'timezone': -10800,
#  'visibility': 10000,
#  'weather': [{'description': 'céu limpo',
#               'icon': '01d',
#               'id': 800,
#               'main': 'Clear'}],
#  'wind': {'deg': 296, 'gust': 6.1, 'speed': 4.3}}
