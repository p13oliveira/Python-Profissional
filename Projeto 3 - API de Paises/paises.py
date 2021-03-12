import json
import sys

import requests

URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name'


def requisição(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
    except Exception:
        print(f"Erro ao fazer requisição: {url}")


def parsing(resp_texto):
    try:
        return json.loads(resp_texto)
    except Exception:
        print("Erro ao fazer parsing.")


def contagem_paises():
    resposta = requisição(URL_ALL)
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            return len(lista_paises)


def listar_paises(lista_paises):
    for pais in lista_paises:
        print(pais['name'])


def mostrar_populacao(nome_pais):
    resp = requisição(f"{URL_NAME}/{nome_pais}")
    if resp:
        lista_paises = parsing(resp)
        if lista_paises:
            for pais in lista_paises:
                print(f"{pais['name']}: {pais['population']} habitantes.")
    else:
        print(f"País não encontrado: {nome_pais}")


def mostrar_moedas(nome_pais):
    resp = requisição(f"{URL_NAME}/{nome_pais}")
    if resp:
        lista_paises = parsing(resp)
        if lista_paises:
            for pais in lista_paises:
                print(f'\nMoedas de {pais["name"]}')
                moedas = pais['currencies']
                for moeda in moedas:
                    print(f'    {moeda["name"]}: {moeda["code"]}')
    else:
        print(f"País não encontrado: {nome_pais}")


def ler_nome_pais():
    try:
        nome_pais = sys.argv[2]
        return nome_pais
    except Exception:
        print("É preciso passar o nome do país.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("## Bem-vindo ao sistema de países ##")
        print("Uso: python paises.py <ação> <nome_país>")
        print("Ações disponíveis: contagem, moeda, população")
    else:
        argumento1 = sys.argv[1]
        if argumento1 == "contagem":
            count = contagem_paises()
            print(f"Existem {count} países no mundo todo.")
        elif argumento1 == "moeda":
            pais = ler_nome_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Argumento Inválido!")

    # ARGPARSE para executar de melhor forma
