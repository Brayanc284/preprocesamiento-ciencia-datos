import time
import math
import numpy as np

def es_primo_np(n):
    if n < 2:
        return False
    limite = int(np.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

inicio = time.time()

numeros = np.arange(1, 100001)
primos_np = [n for n in numeros if es_primo_np(n)]

fin = time.time()

print("Tiempo optimizado con NumPy:", fin - inicio, "segundos")

