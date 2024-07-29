print("Selecione a Instituição de Ensino: ")

escolas = {
    '1': 'Costa Viana',
    '2': 'Unidade Polo',
    '3': 'Herbert',
    '4': 'Adventista'
}

for numero, nome in escolas.items():
    print(f"{numero} - {nome}")

print("====================================================================")

selecionar_instituicao = input("Digite o número da sua Instituição de Ensino: ")

if selecionar_instituicao in escolas:
    print(f"Você selecionou {escolas[selecionar_instituicao]}.")
else:
    print("Valor Inválido!")
    exit()

print("====================================================================")

opcoes = {
    '1': 'LOGIN PROFESSOR',
    '2': 'REGISTRAR PROFESSOR'
}

for numero, opcao in opcoes.items():
    print(f"{numero} - {opcao}")

print("====================================================================")

selecionar_opcao = input("Selecione a opção que deseja: ")

if selecionar_opcao == '1':
    usuario = input("USUARIO: ")
    senha = input("SENHA: ")
    # Aqui você pode adicionar a lógica para login do professor
elif selecionar_opcao == '2':
    nome = input("Digite seu Nome para registro: \n")
    cpf = input("Digite seu CPF (APENAS UMA CONTA POR CPF): \n")
    senha = input("Digite uma Senha: \n")
    # Aqui você pode adicionar a lógica para registrar o professor
else:
    print("Valor Inválido!")
    exit()

print("====================================================================")