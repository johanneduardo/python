#pedir para o usuario dar uma entrada do tipo inteiro

x = int(input("Digite um numero de 1 a 10: "))


i = 0

while x >= 0 or x <=10:
    if x < 0 or x > 10: 
        print("Você errou, tente novamente:")
        x = int(input("Digite um número de 1 a 10: ")) 
    else: 
        print("VOCÊ ACERTOU!!")
        break

