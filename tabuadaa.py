#while, nao sabe quantas vezes o laco vai rodar  ex =  nota valida while
#for seria legal para tabuada, numero determinado


n1 = int(input("Digite um Número para tabuada: "))

i = 0

for i in range (1 , 11):
    print(f"{n1} * {i} == {n1 * i}")
    i = i + 1