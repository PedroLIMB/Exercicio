import unittest
from banco import Conta, Banco, SaldoInsuficiente

class TesteConta(unittest.TestCase):
    
    def setUp(self):
        # Configuração inicial para cada teste na classe Conta
        self.conta = Conta("Cristiano Ronaldo", 100)

    def teste_depositar(self):
        # Teste para verificar se o método depositar funciona corretamente
        self.conta.depositar(50)
        self.assertEqual(self.conta.consultar_saldo(), 150)

    def teste_sacar(self):
        # Teste para verificar se o método sacar funciona corretamente
        self.conta.sacar(50)
        self.assertEqual(self.conta.consultar_saldo(), 50)

    def teste_saldo_insuficiente(self):
        # Teste para verificar se uma exceção SaldoInsuficiente é levantada ao tentar sacar mais do que o saldo disponível
        with self.assertRaises(SaldoInsuficiente):
            self.conta.sacar(150)

class TesteIntegracao(unittest.TestCase):

    def teste_criar_conta_depositar_sacar(self):
        # Teste de integração para criar uma conta, depositar e sacar dinheiro
        conta = Conta("Pedro", 7)

        conta.depositar(50)
        self.assertEqual(conta.consultar_saldo(), 57)
        
        conta.sacar(50)
        self.assertEqual(conta.consultar_saldo(), 7)

if __name__ == '__main__':
    unittest.main()