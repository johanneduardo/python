n1 = float (input("Digite sua primeira nota: "))
n2 = float (input("Digite sua segunda nota: "))
n3 = float (input("Digite sua terceira nota: "))
n4 = float (input("Digite sua quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7.0:
    print(f"Parabens, voce foi aprovado! Sua nota final é {media} ")
else :
    print(f"Nã foi dessa vez... Reprovado. Nota final: {media}")