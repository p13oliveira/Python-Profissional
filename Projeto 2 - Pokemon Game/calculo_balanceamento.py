# Calculo de ataque_inicial

def ataque_minimo(ataque_efetivo, dano_ataque):
    if ataque_efetivo == 0:
        return ataque_efetivo
    elif ataque_efetivo < dano_ataque:
        ataque_efetivo = dano_ataque + ataque_efetivo
        return ataque_efetivo


for i in range(1, 11):
    i = int(i)
    print(f"Pokemon Nv.{i}")
    ataque_inicial_minimo = int((3 * i) + (2 * i * 0.1))
    print(f"Ataque Inicial Minimo: {ataque_inicial_minimo}")
    variacao_minima = int(ataque_inicial_minimo * 0.1 * 1.3)
    variacao_minima = ataque_minimo(variacao_minima, ataque_inicial_minimo)
    print(f"Dano Minimo: {variacao_minima}")
    variacao_maxima = int(ataque_inicial_minimo * 1 * 1.3)
    print(f"Dano Minimo: {variacao_maxima}")
    print("-----------------------------------------------------")
    ataque_inicial_maximo = int((3 * i) + (2 * i * 1))
    print(f"Ataque Inicial Maximo: {ataque_inicial_maximo}")
    variacao_minima = int(ataque_inicial_maximo * 0.1 * 1.3)
    variacao_minima = ataque_minimo(variacao_minima, ataque_inicial_minimo)
    print(f"Dano Minimo: {variacao_minima}")
    variacao_maxima = int(ataque_inicial_maximo * 1 * 1.3)
    print(f"Dano Minimo: {variacao_maxima}")
    print("*******************************************")

# Calculo de vida_inicial
"""
for i in range(1, 11):
    i = int(i)
    print(f"Pokemon Nv.{i}")
    vida_minimo = int((10 * 0.1 * i) + (10 * i))
    print(f"Vida minimo: {vida_minimo}")
    vida_maximo = int((10 * 1 * i) + (10 * i))
    print(f"vida Maximo: {vida_maximo}")
    print()
"""

# Valores iniciais
"""
LVL 01	Variação_Ataque_Inicial = 03 - 5		|	Vida = 11 - 20
LVL 02	Variação_Ataque_Inicial = 06 - 10		|	Vida = 22 - 40
LVL 03	Variação_Ataque_Inicial = 09 - 15		|	Vida = 33 - 60
LVL 04	Variação_Ataque_Inicial = 12 - 20		|	Vida = 44 - 80
LVL 05	Variação_Ataque_Inicial = 16 - 25		|	Vida = 55 - 100
LVL 06	Variação_Ataque_Inicial = 19 - 30		|	Vida = 66 - 120
LVL 07	Variação_Ataque_Inicial = 22 - 35		|	Vida = 77 - 140
LVL 08	Variação_Ataque_Inicial = 25 - 40		|	Vida = 88 - 160
LVL 09	Variação_Ataque_Inicial = 28 - 45		|	Vida = 99 - 180
LVL 10	Variação_Ataque_Inicial = 32 - 50		|	Vida = 100 - 200


vida_inicial = (10 * random(0,1) * lvl) + 10 * lvl
ataque_inicial = (3 * lvl) + (2 * lvl * random(0,1)
dano_efetivo = Ataque * random(0,1) * 1,3
"""
