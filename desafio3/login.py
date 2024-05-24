import os

usuarios = [] #Cadastro de Usuários


def login(conta = False):
    while True:
        acao = int(input("Digite 1 para fazer login,\nDigite 2 para cadastrar uma conta e \nDigite 0 para sair: "))  # Qual ação o usuário vai fazer
        match acao:
            case 1:
                os.system("cls") #Limpa o terminal
                print("Login:")
                #Pede usuário e senha
                login = input("Digite seu usuário: ")
                senha = input("Digite sua senha: ")

                for i in usuarios:
                    if i["login"] == login and i["senha"] == senha:
                        print("Bem vindo!")
                        #Login ok 
                        conta = True
                        
                if conta == False:
                    print("Usuário ou senha não cadastrado, tente novamente!")
                else:
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
                usuarios.append(usuario) #Adiciona o usuário no banco de dados
                print("Usuário Cadastrado")
            case 0:
                break
            case _:
                os.system("cls")
                print("Opção Inválida")
    return conta