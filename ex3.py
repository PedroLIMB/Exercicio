#Lista de itens disponiveis
produtos = {
    "camisa": 50.00,
    "celular": 1.200,
    "cubo magico": 30.00,
    "garfo": 15.00,
    "copo": 12.00,
    "pão": 5.00,
    "teclado": 80.00,
}

class Compras:

    def __init__(self):
        self.carrinho = {}

    def adicionar_produto(self):
        while True:
            #Listara os produtos disponiveis para a compra
            print("Produtos disponíveis:")
            for produto, preco in produtos.items():
                print("- {}: R$ {:.2f}".format(produto, preco))
            print("-" * 30)
            #Adicionara o item desejado e a sua quantidade ao carrinho, caso digite sair o usuario voltara a tela de seleção, caso o produto não seja encontrado uma mensagem avisará ao usuario que este item não se encontra neste mercado
            produto = input("Digite o nome do produto (ou 'sair' para finalizar): ").lower()
            if produto == "sair":
                return
            if produto not in produtos:
                print("Produto '{}' não encontrado.".format(produto))
                continue
            quantidade = int(input("Digite a quantidade de {}: ".format(produto)))
            self.carrinho[produto] = self.carrinho.get(produto, 0) + quantidade
            print("-" * 30)
            print("{} ({}) adicionado ao carrinho.".format(produto, quantidade))
            print("-" * 30)
            break

    def visualizar_carrinho(self):
        #Permite a visualização dos itens que estão no carrinho junto com o preço total de tudo
        print("Carrinho de Compras:")
        for produto, quantidade in self.carrinho.items():
            preco = produtos[produto]
            total_item = quantidade * preco
            print("-" * 30)
            print("{0}: {1} x R$ {2:.2f} = R$ {3:.2f}".format(produto, quantidade, preco, total_item))
            print("-" * 30)

    def remover_produto(self):
        #Remove os itens desejados e sua quantidade do carrinho, caso digite sair o usuario voltara para a tela de seleção, caso digite um item que não esta no carrinho o sistema avisará que este item não esta no carrinho, caso o usuario decida tirar mais itens que estão no carrinho o sistema informara que não a essa quantidade de itens no carrinho
        while True:
            produto = input("Digite o nome do produto a ser removido (ou 'sair' para cancelar): ").lower()
            if produto == "sair":
                return
            if produto not in self.carrinho:
                print("Produto '{}' não encontrado no carrinho.".format(produto))
                continue
            quantidade_remover = int(input("Digite a quantidade de {} a remover: ".format(produto)))
            if quantidade_remover > self.carrinho[produto]:
                print("Quantidade máxima para remover de {} é {}.".format(produto, self.carrinho[produto]))
                continue
            self.carrinho[produto] -= quantidade_remover
            if self.carrinho[produto] == 0:
                del self.carrinho[produto]
            print("{} unidades de {} removidas do carrinho.".format(quantidade_remover, produto))
            break

    def calcular_total(self):
        #calcula o total a pagar
        total = 0
        for produto, quantidade in self.carrinho.items():
            preco = produtos[produto]
            total_item = quantidade * preco
            total += total_item
        print("Total a pagar: R$ {:.2f}".format(total))


compras = Compras()

while True:
    #Menu de seleção
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

    else:
        print("Opção inválida. Tente novamente.")