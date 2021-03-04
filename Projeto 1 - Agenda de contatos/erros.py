# Existem 3 tipos de erros
# 1 - Erros de compilação
# 2 - Erros de execução
# 3 - Erros de lógica

try:
    a = float(input("Digite o numero A: "))  # ValueError
    b = float(input("Digite o numero B: "))

    print(a / b)  # ZeroDivisionError
except ValueError as error:
    print("Valor inválido, digite apenas números")
except ZeroDivisionError as error:
    print("Não pode ser feita divisao por zero")
except Exception as error:
    print("Algum erro ocorreu")
    print(error)
finally:  # Sempre vai ser executado no final
    print("Fim do programa")
