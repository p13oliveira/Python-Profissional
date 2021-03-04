# AAA
conjunto_cores = {"Vermelho", "Azul", "Verde"}  # Declarar um conjunto

for cor in conjunto_cores:
    print(cor)  # A cada iteração ele traz um valor diferente, pois nao é ordenado

conjunto_cores.add("Branco")  # Adicionar elemento a um conjunto
conjunto_cores.add("Vermelho")  # Conjunto não pode ter valores repetidos.

conjunto_cores.remove("Branco")  # Remove do conjunto

print(conjunto_cores)