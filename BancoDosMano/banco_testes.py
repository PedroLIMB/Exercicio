import unittest
from banco import Conta, SaldoInsuficiente

#Testes Unitarios
class TesteConta(unittest.TestCase):
    
    
    def teste_depositar(self):
        conta = Conta("Cristiano Ronaldo", 100)
        conta.depositar(50)
        self.assertEqual(conta.consultar_saldo(), 150)

    def teste_Sacar(self):
        conta = Conta("Cassio Ramos", 100)
        conta.sacar(50)
        self.assertEqual(conta.consultar_saldo(), 50)

    def teste_saldo_insuficiente(self):
        conta = Conta("Bluzão", 100)
        with self.assertRaises(SaldoInsuficiente):
            conta.sacar(150)

#Teste de integração
class TesteIntegracao(unittest.TestCase):

    def teste_criar_conta_depositar_sacar(self):
        #Criar Conta
        conta = Conta("Pedro", 7)
        #Depositar
        conta.depositar(50)
        self.assertEqual(conta.consultar_saldo(), 57)
        #Sacar
        conta.sacar(50)
        self.assertEqual(conta.consultar_saldo(), 7)

if __name__ == '__main__':
    unittest.main()