from login import login #Importa a função de Login
import estoque as e #Importa a biblioteca que trata o estoque
import vendas as v

auth = login()
# auth = True
estoque = []
vendas = []

if auth == True:
    while True:
        try:
            #Abre o menu de opções para o usuário
            acao = int(input("Digite o que você deseja fazer: \n1 - Para adicionar Estoque, \n2 - Para ver Estoques, \n3 - Para adicionar Venda, \n4 - Para ver Vendas, \n0 - Sair\n \n"))

            #Testa as opções
            match acao:
                case 0:
                    print("Sistema Fechando")
                    break
                case 1:
                    e.add_estoque(estoque)
                    print("Estoque Adicionado!")
                case 2:
                    e.ver_estoque(estoque)
                case 3:
                    v.add_venda(estoque, vendas)
                case 4:
                    v.ver_vendas(vendas)
                case _:
                    print ("Opção Inválida!")
        except: #trata erro
            print("Opção Inválida")