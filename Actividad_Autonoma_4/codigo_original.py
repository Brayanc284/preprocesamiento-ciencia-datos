import time 

def num_primo (n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def buscar_numeros_primos (limite):
    primos = []
    for num in range(2, limite + 1):
        if num_primo(num):
            primos.append(num)
    return primos

limite = 100000

print(f"Buscando números primos hasta {limite}...")
inicio = time.time()
primos = buscar_numeros_primos(limite)
fin = time.time()

tiempo_total = fin - inicio

print(f"Total de números primos encontrados: {len(primos)}")
print(f"Tiempo total de ejecución: {tiempo_total:.2f} segundos")

