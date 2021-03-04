from agenda import *

# INICIO DO PROGRAMA
carregar()
while True:
    imprimir_menu()
    opcao = int(input("\nEscolha uma opção: "))
    print()
    if opcao == 1:
        mostrar_contatos()
    elif opcao == 2:
        nome_contato = input("Digite o Nome do Contato: ")
        buscar_contato(nome_contato)
    elif opcao == 3:
        nome_contato = input("Digite o Nome do Contato: ")
        try:
            AGENDA[nome_contato]
            print(f"\n>>>> Contato [{nome_contato.capitalize()}]já existe")
            continue  # Volta ao inicio, ou pula o bloco não precisando executar tudo
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(nome_contato, telefone, email, endereco)
    elif opcao == 4:
        nome_contato = input("Digite o Nome do Contato: ")
        try:
            AGENDA[nome_contato]
            print(f"\n>>>> Editando contato [{nome_contato.capitalize()}]")
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(nome_contato, telefone, email, endereco)
        except KeyError:
            print("\n>>>> Contato inexistente")
    elif opcao == 5:
        nome_contato = input("Digite o Nome do Contato: ")
        excluir_contato(nome_contato)
    elif opcao == 6:
        nome_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_arquivo)
    elif opcao == 7:
        nome_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_arquivo)
    elif opcao == 0:
        salvar()
        exit()
    else:
        print("Opção Inválida!")
