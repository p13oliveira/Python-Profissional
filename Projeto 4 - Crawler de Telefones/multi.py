import threading
import time


def fazer_requisicao_web():
    print("Fazendo requisição web...")
    time.sleep(3)
    print("Terminei a requisição")
    return "Final"


thread_1 = threading.Thread(target=fazer_requisicao_web)  # Passar a função sem os (), porque ela é um parametro
thread_1.start()

print("Chegou Aqui")