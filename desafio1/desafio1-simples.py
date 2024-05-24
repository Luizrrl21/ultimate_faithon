import os
bd = [] #Criar banco de dados de usuários

while True:
    # Qual ação o usuário vai fazer
    acao = int(input("Digite 1 para fazer login,\nDigite 2 para cadastrar uma conta e \nDigite 0 para sair: "))
    match acao:
        case 1:
            os.system("cls") #Limpa o terminal
            print("Login:")
            #Pede usuário e senha
            login = input("Digite seu usuário: ")
            senha = input("Digite sua senha: ")

            x = 0
            for i in bd:
                if i["login"] == login and i["senha"] == senha:
                    print("Bem vindo!")
                    #Login ok 
                    x = 1
            if x == 0:
                print("Usuário ou senha não cadastrado")
            else:
                # Aqui fecha o loop e abre o sistema
                break
        case 2:
            #Criar usuário
            os.system("cls") #Limpar terminal
            print("Cadastrar:")
            login = input("Digite seu usuário: ")
            senha = input("Digite sua senha: ")
            usuario = {
                "login" : login,
                "senha" : senha
            }
            bd.append(usuario) #Adiciona o usuário no banco de dados
            print("Usuário Cadastrado")
        case 0:
            break
        case _:
            os.system("cls")
            print("Opção Inválida")