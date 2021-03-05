from tipos_de_pokemon import *

# Declarar Pokemons
meu_pokemon = PokemonFire('Charmander')
rival_pokemon = PokemonEletric('Pikachu')

# Batalha
meu_pokemon.atacar(rival_pokemon)
rival_pokemon.atacar(meu_pokemon)
