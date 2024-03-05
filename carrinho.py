import os
Carrinho_Compras = []

while True:
    print("*" *30)
    print("Bem vindo ao carrinho de compras")
    print("Opções:")
    print("1 - Adicionar produto ao carrinho")
    print("2 - Ver carrinho")
    print("3 - Remover produto do carrinho")
    print("4 - Calcular total")
    print("5 - Sair")
    print("*" *30)

    Opcao = input("Escolha uma opção: ")
    os.system("cls")

    if Opcao == "1":
        Produto = input("Digite o nome do produto: ")
        Preco_Produto = float(input("Digite o preço do produto: "))
        Carrinho_Compras.append({"produto": Produto, "preço": Preco_Produto})
        print(f"{Produto} foi adicionado ao carrinho")

    elif Opcao == "2":
        if not Carrinho_Compras:
            print("Seu carrinho está vazio.")
        else:
            print("Produtos no carrinho:")
            for Item_Carrinho in Carrinho_Compras:
                print(f"{Item_Carrinho['produto']} - R${Item_Carrinho['preço']}")

    elif Opcao == "3":
        Produto = input("Digite o nome do produto que deseja remover: ")
        for item in Carrinho_Compras:
            if item["produto"] == Produto:
                Carrinho_Compras.remove(item)
                print(f"{Produto} removido com sucesso.")
                break
        else:
            print(f"{Produto} não encontrado no carrinho.")

    elif Opcao == "4":
        Total_Carrinho = sum(Item_Carrinho['preço'] for Item_Carrinho in Carrinho_Compras)
        print(f"Total do carrinho: R${Total_Carrinho:.2f}")

    elif Opcao == "5":
        print("Obrigado por usar o carrinho de compras!")
        break

