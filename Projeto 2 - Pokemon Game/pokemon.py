import random


# Classe descreve um determinado objeto, abstrata onde nunca vai ser estanciada
class Pokemon:
    # Método construtor, usado para construir um objeto (Sempre executado quando inicializar)
    # nome=None --> Quer dizer que não é obrigatório definir uma valor para nome
    # O que colocar no cabeçalho sempre vai ser estatido, então nao setar o level aqui
    def __init__(self, especie=None, level=None, nome=None, tipo=None):
        # self.alguma_coisa é quando nos referimos aos atributos desse objeto
        self.especie = especie
        self.level = level
        self.tipo = tipo
        # Declarar nome
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        # Definir level randomicamente
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        # Definir ataque e vida dos pokemons baseados no lvl
        self.dano_ataque = (self.level * 3) + (self.level * 2 * random.random())
        self.vida = int((self.level * 10 * random.random()) + (self.level * 10))

    # Quando printamos um objeto, é isso que ele nos retorna de informação
    def __str__(self):
        return f"[Nv.{self.level}]{self.nome}[HP:{self.vida}]"

    def gerar_pokemon(self):
        if self.tipo == "Água":
            return PokemonWater(self.nome)
        elif self.tipo == "Fogo":
            return PokemonFire(self.nome)
        elif self.tipo == "Elétrico":
            return PokemonEletric(self.nome)

    def ataque_min(self, ataque_efetivo):
        if int(ataque_efetivo) < 1:
            return 0
        elif ataque_efetivo <= self.dano_ataque:
            min_ataque_efetivo = self.dano_ataque + ataque_efetivo
            return int(min_ataque_efetivo)
        else:
            return int(ataque_efetivo)

    # Ataques durante a batalha
    def atacar(self, pokemon):
        # Reduzir a vida do pokemon
        # RNG do ataque e esquiva
        ataque_efetivo = int(self.dano_ataque * random.random() * 1.3)
        # Minimo de um ataque baseado no seu lvl
        ataque_efetivo = self.ataque_min(ataque_efetivo)
        if ataque_efetivo == 0:
            print(f">>>> {pokemon} esquivou-se!\n")
        else:
            pokemon.vida -= ataque_efetivo
            print(f">>>> {pokemon} perdeu {ataque_efetivo} de vida\n")
        # Continuar lutando até declarar um vencedor
        if pokemon.vida <= 0:
            print("--------------------------------------------")
            print(f"+++ {pokemon} foi derrotado! +++")
            print("--------------------------------------------")
            return True
        else:
            return False


# Herança - Classe filha de Pokemon, onde recebe todas as caracteristicas de Pokemon
class PokemonEletric(Pokemon):

    # Polimorfismo --> Mudar as classes fisicas da classe pai
    def atacar(self, pokemon):
        print(f"{self} usou: CHOQUE DO TROVÃO! em {pokemon}")
        return super().atacar(pokemon)


# Herança - Classe filha de Pokemon, onde recebe todas as caracteristicas de Pokemon
class PokemonFire(Pokemon):

    # Polimorfismo --> Mudar as classes fisicas da classe pai
    def atacar(self, pokemon):
        print(f"{self} usou: BOLA DE FOGO! em {pokemon}")
        return super().atacar(pokemon)


class PokemonWater(Pokemon):

    # Polimorfismo --> Mudar as classes fisicas da classe pai
    def atacar(self, pokemon):
        print(f"{self} usou: JATO DE AGUA! em {pokemon}")
        return super().atacar(pokemon)
