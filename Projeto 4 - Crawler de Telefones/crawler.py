import re
import threading
import requests
from datetime import datetime
from bs4 import BeautifulSoup

DOMINIO = "https://django-anuncios.solyd.com.br"
URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"
LINKS = []
TELEFONES = []
QTDE_THREADS = 5


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Erro ao fazer requisição")
    except Exception as error:
        print("Erro ao fazer requisição")
        print(error)


def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as error:
        print("Erro ao fazer o parsing HTML")
        print(error)


def encontrar_links(soup):
    try:
        cards_pai = soup.find("div", class_="ui three doubling link cards")
        cards = cards_pai.find_all("a")
    except:
        print("Erro ao encontrar links")
        return None

    links = []
    for card in cards:
        try:
            link = card['href']
            links.append(link)
        except:
            pass

    return links


def encontrar_telefone(soup):
    try:
        descricao = soup.find_all("div", class_="sixteen wide column")[2].p.get_text().strip()
    except:
        print("Erro ai encontrar descricao")
        return None

    regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})", descricao)
    if regex:
        return regex


def descobrir_telefones():
    # As threds vão fica executando infinitamente
    while True:
        try:
            link_anuncio = LINKS.pop(0)
        except:
            return None
        resposta_anuncio = requisicao(DOMINIO + link_anuncio)
        if resposta_anuncio:
            soup_anuncio = parsing(resposta_anuncio)
            if soup_anuncio:
                telefones = encontrar_telefone(soup_anuncio)
                if telefones:
                    for telefone in telefones:
                        print(f"Telefone encontrado: {telefone}")
                        TELEFONES.append(telefone)
                        salvar_telefones(telefone)


def salvar_telefones(telefone):
    string_telefone = f"({telefone[0]}){telefone[1]}-{telefone[2]}\n"
    try:
        with open('telefones.csv', 'a') as arquivo:
            arquivo.write(string_telefone)
    except Exception as error:
        print(f"Erro ao salvar arquivo: {error}")


if __name__ == "__main__":
    inicio = datetime.now()  # Calcular tempo de execução do código
    resposta_busca = requisicao(URL_AUTOMOVEIS)
    if resposta_busca:
        soup_busca = parsing(resposta_busca)
        if soup_busca:
            LINKS = encontrar_links(soup_busca)
            # Declarar uma lista de Threds

            THREADS = []
            # Criar threads
            for i in range(QTDE_THREADS):
                t = threading.Thread(target=descobrir_telefones)
                THREADS.append(t)

            # Iniciar as threads
            for t in THREADS:
                t.start()

            # Aguardar as threads
            for t in THREADS:
                t.join()

    # Só executa depois que as threds terminarem
    fim = datetime.now()
    print("-----------------------------")
    print(f"Executou em: {(fim - inicio).total_seconds()} segundos.")
    print("-----------------------------")
    print(TELEFONES)
