#Solicita a quantidade desejada
N = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

#Inicializa od dois primeiros termos
a, b = 0, 1

print("Sequência de Fibonacci:")

for i in range(N):
    print(a, end=", " if i < N - 1 else "\n")
    a, b = b, a + b
