#append, adicionar nome dentro da nossa lista
#insert, alem de receber dados, voce pode mudar o index o qual voce coloca o dado
nomes = []
while True:
    nome = input ("Qual seu nome: ")
    if nome == '-1':
        break

    nomes.append(nome)

print(nomes)