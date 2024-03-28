import unittest
from banco import Conta, Banco, SaldoInsuficiente
 
class TesteConta(unittest.TestCase):
   
    def setUp(self):
        # Configuração inicial para cada teste na classe Conta
        self.conta = Conta("Cristiano Ronaldo", 100)
        self.banco = Banco()
 
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
   
    def test_criar_conta_com_deposito_inicial(self):
        conta_teste = self.conta
        self.banco.CriarConta(conta_teste)
 
        # Verificar se a conta foi criada corretamente
        self.assertEqual(conta_teste.titular, "Cristiano Ronaldo")
        self.assertEqual(conta_teste.saldo, 100)
 
        # Verificar se a conta existe no banco de dados
        self.banco.cursor.execute("SELECT * FROM banco WHERE nome=?", ("Cristiano Ronaldo",))
        conta_banco = self.banco.cursor.fetchone()
        self.assertIsNotNone(conta_banco)
        self.assertEqual(conta_banco[1], "Cristiano Ronaldo")  
 
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