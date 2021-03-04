# TO DO fazer primeiro método (Tipo uma marcação)
AGENDA = {}  # Variável global

AGENDA['pedro'] = {
    'telefone': '99999-0505',
    'email': 'pedro@gmail.com',
    'endereco': 'Av. 1',
}

AGENDA['maria'] = {
    'telefone': '99999-0808',
    'email': 'maria@gmail.com',
    'endereco': 'Av. 2',
}


# Método é uma função
def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(nome_contato):
    print(f'Nome: {nome_contato.capitalize()}')  # Primeira letra maiscula
    print(f'Telefone: {AGENDA[nome_contato]["telefone"]}')
    print(f'E-mail: {AGENDA[nome_contato]["email"]}')
    print(f'Endereço: {AGENDA[nome_contato]["endereco"]}')
    print('----------------------------------------------------------------')


def incluir_editar_contato(nome_contato, telefone, email, endereco):
    AGENDA[nome_contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(f"\n>>>> Contato [{nome_contato.capitalize()}] adicionado/editado com sucesso!")


def excluir_contato(nome_contato):
    AGENDA.pop(nome_contato)
    print(f'\n>>>> Contato [{nome_contato.capitalize()}] excluido com sucesso!')


def imprimir_menu():
    print('\n--------- Minha Agenda ---------')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contatos')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir Contato')
    print('0 - Fechar Agenda')
    print('--------------------------------')


incluir_editar_contato('joao', '99999-3636', 'joao@gmail.com', 'Av. 5', )
incluir_editar_contato('pedro', '99999-5555', 'pedro@gmail.com', 'Av. 2', )
incluir_editar_contato('josé', '99999-6666', None, None, )

while True:
    imprimir_menu()
    opcao = int(input("\nEscolha uma opção: "))
    if opcao == 1:
        mostrar_contatos()
    elif opcao == 2:
        nome_contato = input("Digite o Nome do Contato: ")
        buscar_contato(nome_contato)
    elif opcao == 3 or opcao == 4:
        nome_contato = input("Digite o Nome do Contato: ")
        telefone = input("Digite o Telefone: ")
        email = input("Digite o E-mail: ")
        endereco = input("Digite o Endereço: ")
        incluir_editar_contato(nome_contato, telefone, email, endereco)
    elif opcao == 5:
        nome_contato = input("Digite o Nome do Contato: ")
        excluir_contato(nome_contato)
    elif opcao == 0:
        exit()
    else:
        print("Opção Inválida!")
