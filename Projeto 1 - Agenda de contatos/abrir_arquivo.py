# Não é a melhor forma
"""try:
    arquivo_email = open('email.txt')
    # conteudo = arquivo_email.read()  # Read le o arquivo como uma unica string
    conteudo = arquivo_email.readlines()  # Transforma o conteudo do arquivo em uma lista (adiciona um \n no final)
    print("Lendo Arquivo:")
    for linha in conteudo:
        print(linha.strip())  # Limpa os espaços e os \n - Traz a string limpa
except FileNotFoundError:
    print(">>>> Arquivo não encontrado")
except Exception as error:
    print(f"Ocorreu um erro desconhecido: {error}")
finally:
    arquivo_email.close()"""

# Maniera Correta
try:
    with open('emails.txt') as arquivo_emails:
        conteudo = arquivo_emails.readlines()  # Transforma o conteudo do arquivo em uma lista (adiciona um \n no final)
        print("Lendo Arquivo:")
        for linha in conteudo:
            print(linha.strip())  # Limpa os espaços e os \n - Traz a string limpa
except FileNotFoundError:
    print("\n>>>>Arquivo não existe...")

'''    
'r' - abre para ler
'w' - abre para escrever / arquivo é sobrescrito
'a' - abre para escrever / novo conteudo é adicionao ao final do arquivo
'+' - Adicionar outras funções
'b' - Bińario
'''
