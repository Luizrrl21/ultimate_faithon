import os

def add_estoque(lista:list):
    os.system("cls")
    print("Adicionando Produto")
    codigo = str(input("Digite o código do Produto: "))
    nome = str(input("Digite o nome do Produto: "))
    preco = float(input("Preço do Produto: R$"))
    quantidade = float(input("Quantidade do Produto: "))

    item = {
        "codigo" : codigo,
        "nome" : nome,
        "preco" : preco,
        "quantidade" : quantidade
    }

    lista.append(item)

def ver_estoque(lista):
    os.system("cls")
    print("Controle de Estoque: ")
    if lista == "":
        "Adicione um produto primeiro!"
    else:
        for i in lista:
            print(f"""
        Código: {i["codigo"]},
        Nome: {i["nome"]},
        Preço: R${i["preco"]},
        Quantidade: {i["quantidade"]}

    ------------------------------------
    """)
        
    
