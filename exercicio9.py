def encontrar_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def numero_perfeito(n):
    divisores = encontrar_divisores(n)
    return sum(divisores) == n

def encontrar_numeros_perfeitos(limite):
    perfeitos = []
    for i in range(1, limite + 1):
        if numero_perfeito(i):
            perfeitos.append(i)
    return perfeitos

# Encontrar números perfeitos entre 1 e 10000
limite = 10000
numeros_perfeitos = encontrar_numeros_perfeitos(limite)
print(f"Números perfeitos entre 1 e {limite}: {numeros_perfeitos}")
