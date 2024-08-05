nome_lista = ['PEDRO', 'JOAO', 'LUCAX', 'MARCIELITO']

nome_pessoa = input('Escreva seu nome e veja se ele faz parte da lista')

if nome_pessoa in nome_lista:
    print(f'Seu nome faz parte da lista.')
else:
    print('Seu nome não esta na lista')