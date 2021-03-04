# TO DO fazer primeiro método (Tipo uma marcação)
AGENDA = {}  # Variável global


# Método é uma função
def mostrar_contatos():
    if AGENDA:
        print('-------- Contatos --------')
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print(">>>> Agenda Vazia")


def buscar_contato(nome_contato):
    try:
        print(f'Nome: {nome_contato.capitalize()}')  # Primeira letra maiscula
        print(f'Telefone: {AGENDA[nome_contato]["telefone"]}')
        print(f'E-mail: {AGENDA[nome_contato]["email"]}')
        print(f'Endereço: {AGENDA[nome_contato]["endereco"]}')
        print('----------------------------------------------------------------')
    except KeyError:
        print(">>>> Contato Inexistente")
    except Exception as error:
        print(f"Um erro inesperado ocorreu: {error}")


def ler_detalhes_contato():
    telefone = input("Digite o Telefone: ")
    email = input("Digite o E-mail: ")
    endereco = input("Digite o Endereço: ")
    return telefone, email, endereco


def incluir_editar_contato(nome_contato, telefone, email, endereco):
    try:
        AGENDA[nome_contato]  # Verificar se o contato existe
    except KeyError:
        AGENDA[nome_contato] = {
            'telefone': telefone,
            'email': email,
            'endereco': endereco,
        }
        salvar()
        print(f">>>> Contato [{nome_contato.capitalize()}] adicionado/editado com sucesso!")
    except Exception as error:
        print(f"Um erro inesperado ocorreu: {error}")


def excluir_contato(nome_contato):
    try:
        AGENDA.pop(nome_contato)
        salvar()
        print(f'>>>> Contato [{nome_contato.capitalize()}] excluido com sucesso!')
    except KeyError:
        print(">>>> Contato Inexistente")
    except Exception as error:
        print(f"Um erro inesperado ocorreu: {error}")


def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo_agenda:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo_agenda.write(f'{contato};{telefone};{email};{endereco}\n')
        print(f">>>> Agenda exportada com sucesso")
    except Exception as error:
        print(f">>>> Algum erro ocorreu ao exportar contatos: {error}")


def importar_contatos(nome_arquivo):
    try:
        with open(f"{nome_arquivo}", 'r') as arquivo_contatos:
            linhas = arquivo_contatos.readlines()
            for indice, linha in enumerate(linhas):
                detalhes = linha.strip().split(";")
                nome_contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome_contato, telefone, email, endereco)
        print(f'>>>> {len(AGENDA)} contatos carregados com sucesso')
    except FileNotFoundError:
        print(">>>> Arquivo não encontrado")
    except Exception as error:
        print(f"Ocorreu um erro: {error}")


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open(f"database.csv", 'r') as arquivo_contatos:
            linhas = arquivo_contatos.readlines()
            for indice, linha in enumerate(linhas):
                detalhes = linha.strip().split(";")

                nome_contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome_contato] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('>>>> Database carregado com sucesso')
        print(f'>>>> {len(AGENDA)} contatos carregados com sucesso')
    except FileNotFoundError:
        print(">>>> Arquivo não encontrado")
    except Exception as error:
        print(f"Ocorreu um erro: {error}")


def imprimir_menu():
    print('\n--------- Minha Agenda ---------')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contatos')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir Contato')
    print('6 - Exportar contatos CSV')
    print('7 - Importar contatos CSV')
    print('0 - Fechar Agenda')
    print('--------------------------------')
