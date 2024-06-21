import requests

import os, sys    

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path[:current_path.find(os.path.dirname(__file__))]
sys.path.append(current_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cer3.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from backend.models import Pokemon

def obtener_datos_de_api(url):
    # Realiza una petición GET a la URL proporcionada
    response = requests.get(url)

    # Verifica que la petición se haya realizado correctamente
    if response.status_code == 200:
        try:
            # Intenta convertir la respuesta JSON en una lista de diccionarios
            data = response.json()
            return data
        except ValueError:
            # Maneja el caso donde la respuesta no es un JSON válido
            print("Error: No se pudo decodificar el JSON")
    else:
        # Imprime el código de estado HTTP si la petición no fue exitosa
        print(f"Error: La petición HTTP falló con el código {response.status_code}")

# URL de la API
url_api = 'https://pokeapi.co/api/v2/pokemon?limit=151'
# 'https://pokeapi.co/api/v2/pokemon/1'

# Obtiene los datos de la API
datos_recibidos = obtener_datos_de_api(url_api)

pokemons = datos_recibidos['results']

for pokemon in pokemons:
    name = pokemon['name']
    poke_data = obtener_datos_de_api(pokemon['url'])
    pokedex_number = poke_data['id']
    primary_type = poke_data['types'][0]['type']['name']
    secondary_type = None
    if len(poke_data['types']) > 1:
        secondary_type = poke_data['types'][1]['type']['name']
    # print(name, pokedex_number, primary_type, secondary_type)

    poke_db, _ = Pokemon.objects.get_or_create(
        name = name,
        pokedex_number = pokedex_number,
        primary_type = primary_type,
        secondary_type = secondary_type
    )

    print(poke_db)