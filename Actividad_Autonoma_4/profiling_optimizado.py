import cProfile
import pstats
import math

def es_primo_opt(n):
    if n < 2:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

def ejecutar():
    primos = [num for num in range(1, 100001) if es_primo_opt(num)]

cProfile.run("ejecutar()", "profiling_optimizado.txt")

p = pstats.Stats("profiling_optimizado.txt")
p.sort_stats("tottime")
p.print_stats()
