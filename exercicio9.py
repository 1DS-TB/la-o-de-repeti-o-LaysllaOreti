soma = 0

for num in range(1,10001):

    for i in range(1,num):
        if num % i == 0:
            soma += i
    if soma == num:
        print(f"O número {num} é perfeito")

    soma -= soma
