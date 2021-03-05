from tipos_de_pokemon import PokemonEletric


class Pikachu(PokemonEletric):
    especie = "Pikachu"

    # Polimorfismo --> Mudar as classes fisicas da classe pai
    def atacar(self, pokemon):
        print(f"{self} usou: JATO DE AGUA! em {pokemon}")
