print('Calculador de Médias! \n')


x = [float(input(f'Digite sua média {i+1}: ')) for i in range(3)]


media = sum(x) / len(x)

if media >= 6.0:
    print(f'Aprovado! Sua média foi {media:.2f}')
else:
    print(f'Reprovado. Sua média foi {media:.2f}')
