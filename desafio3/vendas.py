import os

def add_venda(estoque: list, vendas: list):
    os.system("cls") #Limpa Terminal
    print("Registrando Venda: ") 
    codigo = str(input("Digite o código do Produto: ")) #Produto a ser vendido
    for i in estoque: #Iteração no Estoque
        if i["codigo"] == codigo: #Condicional para achar produto
            print(f"Estoque Disponível: {i['quantidade']} unidades") #Estoque Disponível
            pedido = int(input("Quantidade vendida: ")) #Quantidade Vendida
            if pedido > i["quantidade"]: #Verifica se tem Estoque
                print("Produto indisponível!")
            else:
                i["quantidade"] -= pedido
                valor = float(pedido * i["preco"]) #Valor da venda

                venda = {
                    "codigo" : codigo,
                    "nome" : i["nome"],
                    "pedido": pedido,
                    "valor": valor
                }

                vendas.append(venda) #Registra a Venda
                print("Venda Registrada!")

def ver_vendas(vendas: list):
    os.system("cls") #Limpa terminal
    quantidade = len(vendas) #Pega quantas vendas foram feitas
   
    valor = [] #Itera e adiciona na lista apenas os valores das vendas
    for i in vendas:
        valor.append(i["valor"])

    print(f"Quantidade de Vendas: {quantidade}")
    print(f"Total vendido: R${sum(valor)}")

