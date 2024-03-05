import os

dicio_carrinho = {}

# Classe Compras

class Compras:

    def __init__(self):
        self.carrinho = {}

    def adicionar_produto(self):
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$ "))
        self.carrinho[produto] = preco
        print(f"{produto} foi adicionado ao carrinho")

    def visualizar_carrinho(self):
        print("Carrinho de Compras:")
        for produto, preco in self.carrinho.items():
            print(f"{produto}: R$ {preco}")
        print("-" * 30)

    def remover_produto(self):
        produto_remover = input("Digite o nome do produto a ser removido: ")
        if produto_remover in self.carrinho:
            del self.carrinho[produto_remover]
            print(f"{produto_remover} foi removido do carrinho")
        else:
            print(f"{produto_remover} não encontrado no carrinho")

    def calcular_total(self):
        total = sum(self.carrinho.values())
        print(f"Total a pagar: R$ {total:.2f}")

compras = Compras()

# Opções

while True:
    print("*" * 30)
    print("Bem vindo ao carrinho de compras")
    print("Opções:")
    print("1 - Adicionar produto ao carrinho")
    print("2 - Ver carrinho")
    print("3 - Remover produto do carrinho")
    print("4 - Calcular total")
    print("5 - Sair")
    print("*" * 30)

    opcao = input("Escolha uma opção: ")
    os.system("cls")

    if opcao == "1":
        compras.adicionar_produto()

    elif opcao == "2":
        compras.visualizar_carrinho()

    elif opcao == "3":
        compras.remover_produto()

    elif opcao == "4":
        compras.calcular_total()

    elif opcao == "5":
        break