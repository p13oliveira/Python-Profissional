"""
Os imports são separados em 3 niveis
1) import random --> Bibliotecas built-in
2) import bibliotecas_pip --> Importa as bibliotecas do pip, as instaladas no caso
3) import local --> Imports dos metodos locais do programa
"""
import pickle

from pessoa import *


def escolher_pokemon_inicial(player):
    print(f"\n{player}, agora você precisar escolher o pokemon que irá lhe acompanhar nessa jornada!")
    print("Portanto escolha um com bastante cuidado.")
    pikachu = PokemonEletric("Pikachu", level=1)
    charmeleon = PokemonFire("Charmilion", level=1)
    squirtle = PokemonWater("Squirtle", level=1)
    print("\nVocê possui 3 escolhas: ")
    print(f"1 - {pikachu}")
    print(f"2 - {charmeleon}")
    print(f"3 - {squirtle}")
    while True:
        escolha = int(input("\nEscolha seu Pokemon: "))
        if escolha == 1:
            player.capturar(pikachu)
            break
        elif escolha == 2:
            player.capturar(charmeleon)
            break
        elif escolha == 3:
            player.capturar(squirtle)
            break
        else:
            print("Opção invalida!")


def salvar_jogo(player):
    try:
        # Salvar um objeto em formato binario
        with open("database.db", 'wb') as arquivo:
            pickle.dump(player, arquivo)  # Transforma os dados em bytes
            print(">> Jogo salvo com sucesso!\n")
    except Exception as error:
        print(">> Erro ao salvar o jogo!\n")
        print(error)


def carregar_jogo():
    try:
        # Salvar um objeto em formato binario
        with open("database.db", 'rb') as arquivo:
            player = pickle.load(arquivo)  # Transforma os dados em bytes
            print("\n>> Save carregado com sucesso!\n")
            return player
    except Exception as error:
        print("\n>> Save não encontrado!")


# Função principal para executar ("Classe Main")
# Só vai executar esse função principal, quando executar esse arquivo
if __name__ == "__main__":
    print("---------------------------------------")
    print("Bem-vindo ao game Pokemon RPG em Python")

    player = carregar_jogo()

    # Se não existir jogador, fazer a abertura do game
    if not player:
        nome = input("\nOlá, qual é o seu nome:\n")
        player = Player(nome)
        print(f"\nOlá {nome}, esse é um mundo habitado por pokemons, "
              f"a partir de agora sua missão é se tornar um mestre dos pokemons.")
        print("Capture o máximo de pokemons que conseguir e lute com seus inimigos em grandes batalhas.")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("já vi que você tem alguns pokemons")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokemon, portando precisa escolher um.")
            print("Vamos lá...")
            escolher_pokemon_inicial(player)

        print(
            "Pronto, agora que você já possui um pokemon, enfrente seu arqui-rival desde o jardim da infância, Pedro.\n")
        pedro = Inimigo(nome="Pedro", pokemons=[PokemonFire("Charmeleon", level=2)])
        if player.batalhar(pedro):
            print("Não fique assim, todos perdemos e ganhamos.")
            print("Agora é erguer a cabeça, e vamos explorar esse mundo vasto repleto de pokemons.")
            print("Boa sorte!!!\n")
        else:
            print("Olha quem diria, você leva muito jeito para ser um grande treinador pokemon")
            print("Boa sorte nessa sua nova jornada!!!\n")
        salvar_jogo(player)

    while True:
        print("------ Pokemon Game Pyton ------")
        print("1 - Explorar o mundo")
        print("2 - Batalhar")
        print("3 - Ver Pokeagenda")
        print("0 - Sair do jogo")
        op = input("Escolha: ")

        if op == "0":
            salvar_jogo(player)
            print("\nFechando o jogo...")
            exit()
        elif op == "1":
            player.explorar(player)
            salvar_jogo(player)
        elif op == "2":
            oponente = Inimigo()
            player.batalhar(oponente)
            salvar_jogo(player)
        elif op == "3":
            player.mostrar_pokemons()
        else:
            print("Escolha inválida")
