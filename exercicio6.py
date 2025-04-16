num = int(input("Digite quantos termos você deseja: "))
a = 1
b = 0
contador = 0
fibonnaci = []

if num < 1:
    print("INVALIDO")
else:
    while contador < num:
        a,b = b,a+b
        fibonnaci.append(a)
        contador +=1
print(fibonnaci)
