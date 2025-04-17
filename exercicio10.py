numero1 = int(input("Digite o primeiro intervalo: "))
numero2 = int(input("Digite o segundo intervalo: "))

if numero1 <= 0 or numero2 <= 0:
    print("Inválido")
else:
    for i in range (numero1, numero2):
        i2 = str(i**2)
        tamanho = len(i2)

        if i < 10:
            if i == 9 or i == 1:
                print(f"O número {i} é considerado um número Kaprekar.")

        elif tamanho % 2 != 0 or i == 9 or i == 1:
            metade = tamanho // 2
            ladoDireito = tamanho - metade
            ladoEsquerdo = tamanho - lDireita

            direita = int(i2[-ladoDireito:])
            esquerda = int(i2[:ladoEsquerdo])

            if direita + esquerda == i:
                print(f"O número {i} é considerado um número Kaprekar.")

        else:

            metade = tamanho // 2
            ladoDireito = tamanho - metade
            ladoEsquerdo = tamanho - lDireita

            direita = int(i2[-ladoDireito:])
            esquerda = int(i2[:ladoEsquerdo])

            if direita + esquerda == i:
                print(f"O número {i} é um número Kaprekar.")

        metade = 0
        ladoDireito = 0
        ladoEsquerdo = 0
