Numero = int(input("Insira um número: "))

if Numero <1:
    print("INVALIDO")
else:
    for linha in range(1, Numero+1): 
        for cada in range (linha): 
            print("x ", end=" ")
        print(" ") 
