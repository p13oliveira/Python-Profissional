try:
    with open('nomes.txt', 'a') as arquivo_nome:
        arquivo_nome.write('pedro\n'.capitalize())
except Exception as error:
    print(f"Algum erro ocorreu {error}")
