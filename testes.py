import unittest
from unittest.mock import patch
from io import StringIO
from ex3 import Compras, produtos  # Importa a classe Compras e o dicionário produtos
 
class TestCompras(unittest.TestCase):
 
    def setUp(self):
        self.compras = Compras()  # Inicializa uma instância da classe Compras antes de cada teste
  
    def teste_adicionar_produto(self):
        with patch("builtins.input", side_effect=["camisa", "2"]):
            self.compras.adicionar_produto()  # Testa o método adicionar_produto simulando a entrada do usuário
        self.assertEqual(self.compras.carrinho, {"camisa": 2})  # Verifica se o carrinho foi atualizado corretamente

    @patch("sys.stdout", new_callable=StringIO)
    def auxiliar_verificar_carrinho(self, carrinho_final, produto):
        # Método auxiliar que utiliza o patch para redirecionar a saída padrão e verifica se ela corresponde ao esperado
        self.compras.visualizar_carrinho()
        self.assertEqual(produto.getvalue().strip(), carrinho_final.strip())

    def teste_visualizar_carrinho(self):
        self.compras.carrinho = {"camisa": 2, "celular": 1}
        carrinho_final = "Carrinho de Compras:\ncamisa: 2 x R$ 50.00 = R$ 100.00\ncelular: 1 x R$ 1200.00 = R$ 1200.00"
        self.auxiliar_verificar_carrinho(carrinho_final)  # Testa o método visualizar_carrinho e verifica a saída esperada
 
    def teste_remover_produto(self):
        self.compras.carrinho = {"camisa": 2, "celular": 1}
        with patch("builtins.input", side_effect=["camisa", "1"]):
            self.compras.remover_produto()  # Testa o método remover_produto simulando a entrada do usuário
        self.assertEqual(self.compras.carrinho, {"camisa": 1, "celular": 1})  # Verifica se o carrinho foi atualizado corretamente
 
    def teste_calcular_total(self):
        self.compras.carrinho = {"camisa": 2, "celular": 1}
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.compras.calcular_total()  # Testa o método calcular_total e verifica a saída esperada
        total_esperado = 2 * produtos["camisa"] + 1 * produtos["celular"]
        self.assertEqual(mock_stdout.getvalue().strip(), "Total a pagar: R$ {:.2f}".format(total_esperado))
 
if __name__ == "__main__":
    unittest.main()  # Executa os testes quando o script é executado diretamente