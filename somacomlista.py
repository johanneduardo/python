x = [int(input("Digite 10 números para que sejam somados + 1: ")) for i in range (0,10) ]

soma = 0
for i in x:
    soma = soma + i
    print(soma)