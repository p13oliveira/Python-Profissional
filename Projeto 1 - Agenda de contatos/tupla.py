# Tuplas são parecidos com as listas
# Mas ela não permite adicionar mais elementos, elas são estáticas

tupla_cores = ("Azul", "Amarelo", "Verde", "Vermelho", "Roxo", "Branco")
lista_cores = ["Azul", "Amarelo", "Verde", "Vermelho", "Roxo", "Branco"]

# print(tupla_cores)
# print(tupla_cores[1])
# print(tupla_cores[1:3])

lista_cores.append("Marron")

lista_cores[1] = "Laranja"  # Substituir o valor do elemento do indice

print(tupla_cores)
print(lista_cores)
