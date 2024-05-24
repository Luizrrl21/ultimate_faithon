produtos = []

while True:
    acao = int(input("Digite 1 para Cadastrar ou 2 para Consultar: "))
    match acao:
        case 1:
            produto = input("Digite o nome do Produto")