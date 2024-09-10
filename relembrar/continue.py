#continue faz o contario de BREAK, podemos continuar uma função apartir de tal escolha

i = 0

while i < 10:
    print(i)
    if i % 2 == 1:
        i += 2
        continue
    i += 1