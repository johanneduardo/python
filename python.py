print ("Selecione a Instituição de Ensino: ")

escola1 = '1 - Costa Viana'
escola2 = '2 - Unidade Polo'
escola3 = '3 - Herbert'
escola4 = '4 - Adventista'

print (escola1)
print (escola2)
print (escola3)
print (escola4)

print("====================================================================")

selecionar_instituicao = input("Digite o número da sua Instituição de Ensino: ")

if selecionar_instituicao == '1' :
    print (f"Você selecionou {escola1}.")

elif selecionar_instituicao == '2':
    print (f"Você selecionou {escola2}.")

elif selecionar_instituicao == '3':
    print (f"Você selecionou {escola3}.")

elif selecionar_instituicao == '4':
    print (f"Você selecionou {escola4}.")

else:
    print ("Valor Invalido!")
    quit()

print("====================================================================")

a = '1 - LOGIN PROFESSOR'
b = '2 - REGISTRAR PROFESSOR'

print (a)
print (b)


print("====================================================================")

selecionar_opcao = input("Selecione a opção que deseja: ")

usuario = ''
senha = ''
nome = ''
cpf = ''
senha2 = ''

if selecionar_opcao == '1':
    usuario = input("USUARIO: ")
    senha = input("SENHA: ")
    
elif selecionar_opcao == '2':
    nome = input("Digite seu Nome para registro: \n")
    cpf = input("Digite seu CPF (APENAS UMA CONTA POR CPF): \n"   )
    senha2 = input ("Digite uma Senha: ")

else:
    print ("Valor Invalido!")
    quit() 

print("====================================================================")




