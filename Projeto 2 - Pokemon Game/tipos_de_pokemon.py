from pokemon import Pokemon


# Herança - Classe filha de Pokemon, onde recebe todas as caracteristicas de Pokemon
class PokemonEletric(Pokemon):
    tipo = "Eletric"

    # Polimorfismo --> Mudar as classes fisicas da classe pai
    def atacar(self, pokemon):
        print(f"{self} usou: CHOQUE DO TROVÃO! em {pokemon}")


# Herança - Classe filha de Pokemon, onde recebe todas as caracteristicas de Pokemon
class PokemonFire(Pokemon):
    tipo = "Fire"

    # Polimorfismo --> Mudar as classes fisicas da classe pai
    def atacar(self, pokemon):
        print(f"{self} usou: BOLA DE FOGO! em {pokemon}")


class PokemonWater(Pokemon):
    tipo = "Water"

    # Polimorfismo --> Mudar as classes fisicas da classe pai
    def atacar(self, pokemon):
        print(f"{self} usou: JATO DE AGUA! em {pokemon}")
