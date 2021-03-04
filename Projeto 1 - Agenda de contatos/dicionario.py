pessoas = {
    "guilherme": 19,
    "maria": 17,
    "joao": 20
}  # Declaração de um dicionario

# Dicionarios não possuem indice, e sim chaves
print(pessoas["guilherme"])
print()

for pessoa in pessoas:
    print(pessoas[pessoa])  # Percorrer o dicionario pelas chaves
