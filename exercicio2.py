N = int(input("Digite um número inteiro positivo: "))

#Saber sse o número é positivo
while N <= 0:
    N = int(input("Por favor, insira um número inteiro que seja positivo: "))

soma = 0
contador = 1

#Laço para somar os números de 1 até N
while contador <= N:
    soma += contador
    contador += 1

#Exibir o resultado
print(f"A soma de 1 até {N} é: {soma}")
