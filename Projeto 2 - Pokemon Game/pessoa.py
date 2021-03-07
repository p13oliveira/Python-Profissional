from pokemon import *

NOMES = [
    'Ziakar', 'Noadui', 'Keowan', 'Ankoha', 'Fiduan', 'Keielr', 'Vivear', 'Defyus', 'Buevor', 'Hyekoi', 'Foecol',
    'Dieolr', 'Ruoins', 'Ungois', 'Xaokul',
]

POKEMONS = [
    ['Charmander', 'Fogo'], ['Charmeleon', 'Fogo'], ['Charizard', 'Fogo'], ['Vulpix', 'Fogo'], ['Ninetales', 'Fogo'],
    ['Growlithe', 'Fogo'], ['Arcanine', 'Fogo'], ['Ponyta', 'Fogo'], ['Squirtle', 'Água'], ['Wartortle', 'Água'],
    ['Blastoise', 'Água'], ['Psyduck', 'Água'], ['Golduck', 'Água'], ['Tentacool', 'Água'], ['Tentacruel', 'Água'],
    ['Pikachu', 'Elétrico'], ['Raichu', 'Elétrico'], ['Magnemite', 'Elétrico'], ['Magneton', 'Elétrico'],
    ['Voltorb', 'Elétrico'], ['Eletrodo', 'Elétrico']
]


# Construtor pessoa
class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        self.pokemons = pokemons
        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    # listar todos os pokemons
    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"\nPokemons de {self.nome.upper()}:")
            for i, pokemon in enumerate(self.pokemons):
                print(f'  {i + 1}. {pokemon}')
            print("")
        else:
            print(f"{self.nome.upper()} não possui nenhum pokemon.")

    # Escolher pokemon aleatoriamente
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f">>>> {self} escolheu {pokemon_escolhido}")
            return pokemon_escolhido
        else:
            print("Esse jogador não possui nenhum pokemon para ser escolhido...")

    # Recompensa de vitoria por batalha
    def recompensa_batalha(self, quantidade):
        self.dinheiro += quantidade
        print(f">>>> Você ganhou ${quantidade} de moedas.")
        self.mostrar_dinheiro()

    # Exibir o valor das moedas do player
    def mostrar_dinheiro(self):
        print(f">>>> Você possui ${self.dinheiro} de moedas.\n")

    # Inicio da batalha
    def batalhar(self, pessoa):
        print(f">>>> {self} iniciou uma BATALHA com {pessoa}")
        # Inimigo Escolher pokemon
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        # Player escolher pokemon
        pokemon_aliado = self.escolher_pokemon()
        vida_inicial_aliado = pokemon_aliado.vida
        vida_inicial_inimigo = pokemon_inimigo.vida
        # batalha pokemon
        print(">> Inicio da Batalha <<")
        if pokemon_aliado and pokemon_inimigo:
            while True:
                # Vitoria do player
                if pokemon_aliado.atacar(pokemon_inimigo):
                    print(f"\n{self} ganhou a batalha pokemon!\n")
                    self.recompensa_batalha(pokemon_inimigo.level * 10)
                    pokemon_aliado.vida = vida_inicial_aliado
                    pokemon_inimigo.vida = vida_inicial_inimigo
                    return False
                    break
                # Derrota do player
                elif pokemon_inimigo.atacar(pokemon_aliado):
                    print(f"\n{pessoa} ganhou a batalha pokemon!\n")
                    pokemon_aliado.vida = vida_inicial_aliado
                    pokemon_inimigo.vida = vida_inicial_inimigo
                    return True
                    break
        else:
            print(">>>> Essa batalha não pode ocorrer!")


# Comando referentes ao player
class Player(Pessoa):
    tipo = "Player"

    # Escolher pokemon do players
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = input(f"{self} escolha seu Pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha - 1]
                    print(f">>>> {pokemon_escolhido} eu escolho você!!!\n")
                    return pokemon_escolhido
                except:
                    print("Opção invalida!")
        else:
            print("Esse jogador não possui nenhum pokemon para ser escolhido...")

    # Adicionar um Pokemon ao inventario do player
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'\n>>>> {self} CAPTUROU {pokemon}!')

    def explorar(self, player):
        if random.random() <= 0.3:
            if random.random() <= 0.5:
                # Gerar pokemon aleatorio
                tipo_pokemon = random.choice(POKEMONS)
                pokemon = Pokemon(nome=tipo_pokemon[0], tipo=tipo_pokemon[1]).gerar_pokemon()
                print(f"\nUm pokemon selvagem apareceu: {pokemon}")
                # Capturar pokemon
                escolha = input("Deseja capturar o pokemon? (s/n)\n")
                if escolha == "s":
                    if random.random() >= 0.5:
                        self.capturar(pokemon)
                        self.mostrar_pokemons()
                    else:
                        print(f"\n{pokemon} fugiu, que pena!!!\n")
                else:
                    print("\nOK, boa viagem.\n")
            else:
                print("\nOh não! Um inimigo apareceu")
                print("Prepare-se para a batalha!!!\n")
                oponente = Inimigo()
                player.batalhar(oponente)
        else:
            print("\nEssa exploração não deu em nada.\n")


# Comando referentes ao inimigo
class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=None):
        # super() --> instancia a classe pai, onde pode chamar as funções dela
        if not pokemons:
            pokemons_aleatorios = []
            # Gera de 1 a 3 Pokemons aleatórios
            for i in range(random.randint(1, 6)):
                pokemon = random.choice(POKEMONS)
                pokemons_aleatorios.append(Pokemon(nome=pokemon[0], tipo=pokemon[1]).gerar_pokemon())
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)


if __name__ == "__main__":
    Inimigo().mostrar_pokemons()
