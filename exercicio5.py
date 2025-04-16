numb = int(input("Digite um número: "))
divisor = 0

for i in range(1, num +1):
    if numb % i == 0 and num >= 1:
        divisor +=1

if divisor == 2:
    print(f"{numb} eh primo")
elif divisor <1:
    print("INVALIDO")
else:
    print(f"{numb} nao eh primo")
