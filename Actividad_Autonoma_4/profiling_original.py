import cProfile
import pstats

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ejecutar():
    primos = []
    for num in range(1, 100001):
        if es_primo(num):
            primos.append(num)

cProfile.run("ejecutar()", "profiling_original.txt")

p = pstats.Stats("profiling_original.txt")
p.sort_stats("tottime")
p.print_stats()
