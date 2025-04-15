def soma_harmonica(N): #definir a função de soma de série harmônica
    soma = 0 #inicializando a variável agregando valor 0
    for i in range(1, N+1):   #vai percorrer todos os valores de i de 1 até N
        soma += 1/i   #a cada iteração, é adicionado à variável soma
    return round(soma, 2)   #round é a operação de arredondamente do resultado

# Exemplo de uso
N = int(input("Digite o valor de N: "))
resultado = soma_harmonica(N)
print(f"A soma da série harmônica até {N} termos é: {resultado}")