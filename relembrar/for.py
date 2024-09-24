#while e quando nao se tem nocao de quanto tempo o codigo vai rodar

#for como consequencia e quando ja se tem um tamanho "exato"

'''interessante que em for nao precisamos declarar uma variavel para trabalhar, tipo i = 0, comandamos tudo dentro de uma função'''


for i in range (1,11):
    print(f"========== TABUADA {i} =========")
    for j in range (1,11):
        print (f"{i} x {j} == {i * j}")