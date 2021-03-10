import json

import requests

URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name/brazil'

resp = requests.get(URL_ALL)

paises = json.loads(resp.text)  # Parsing de json para python

# print(len(paises))  # Quantidade de paises na lista

for pais in paises:
    print(pais['name'], pais['currencies'])
