def numero_kaprekar(n):
    # Calculando o quadrado do número
    quadrado = n ** 2
    
    # Convertendo o quadrado em string para dividir em duas partes
    quadrado_str = str(quadrado)
    
    # Definindo o tamanho da parte direita (número de dígitos do número original)
    tamanho_direita = len(str(n))
    
    # Parte direita é a quantidade de dígitos do número original
    parte_direita = int(quadrado_str[-tamanho_direita:]) if len(quadrado_str) > tamanho_direita else 0
    
    # Parte esquerda é o restante dos dígitos
    parte_esquerda = int(quadrado_str[:-tamanho_direita]) if len(quadrado_str) > tamanho_direita else 0
    
    # Somando as duas partes
    soma = parte_direita + parte_esquerda
    
    # Se a soma for igual ao número original, é um número de Kaprekar
    return soma == n

# Solicitando ao usuário os limites do intervalo
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

# Encontrando e imprimindo todos os números de Kaprekar no intervalo
print(f"Números de Kaprekar entre {inicio} e {fim}:")
for num in range(inicio, fim + 1):
    if numero_kaprekar(num):
        print(num)
