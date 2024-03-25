import customtkinter as ctk
from tkinter import messagebox
import sqlite3

# Definição da classe para representar uma conta bancária
class Conta():
    def __init__(self, titular, saldo=0):
        self.titular = titular  
        self.saldo = saldo  

    # Método para depositar um valor na conta
    def depositar(self, valor):
        self.saldo += valor

    # Método para sacar um valor da conta
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            raise SaldoInsuficiente()

    # Método para consultar o saldo da conta
    def consultar_saldo(self):
        return self.saldo

# Definição de uma exceção personalizada para saldo insuficiente
class SaldoInsuficiente(Exception):
    pass

# Definição da classe para representar o Banco
class Banco():
    def __init__(self):
        self.banco = sqlite3.connect("bancoDosMano.db")
        self.cursor = self.banco.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS banco (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(80), saldo INTEGER)''')

        self.banco.commit()

    def CriarConta(self, conta):
        try:
            self.cursor.execute("INSERT INTO banco (nome, saldo) VALUES (?, ?)", (conta.titular, conta.saldo,))
            self.banco.commit()
            messagebox.showinfo("Conta Criada", "Conta bancária criada com sucesso.")
        except sqlite3.Error as err:
            messagebox.showerror("Erro", "Erro ao criar conta: " + str(err))

    def Depositar(self, nome, valor):
        try:
            self.cursor.execute("UPDATE banco SET saldo = saldo + ? where nome = ?", (valor, nome))
            self.banco.commit()
            messagebox.showinfo("Depósito", f"Depósito de R${valor} realizado.")
        except sqlite3.Error as err:
            messagebox.showerror("Erro", "Erro ao depositar: " + str(err))

    def Sacar(self, nome, valor):
        try:
            self.cursor.execute("SELECT saldo FROM banco WHERE nome = ?", (nome,))
            saldo_atual = self.cursor.fetchone()[0]
            if saldo_atual >= valor:
                self.cursor.execute("UPDATE banco SET saldo = saldo - ? where nome = ?", (valor, nome))
                self.banco.commit()
                messagebox.showinfo("Saque", f"Saque de R${valor} realizado.")
            else:
                messagebox.showerror("Saldo Insuficiente", "Saldo insuficiente.")
        except sqlite3.Error as err:
            messagebox.showerror("Erro", "Erro ao sacar: " + str(err))

    def VerSaldo(self, nome):
        try:
            self.cursor.execute("SELECT saldo FROM banco WHERE nome = ?", (nome,))
            saldo_atual = self.cursor.fetchone()[0]
            messagebox.showinfo("Saldo Atual", f"O saldo atual da conta é: R${saldo_atual}")
        except sqlite3.Error as err:
            messagebox.showerror("Erro", "Erro ao verificar saldo: " + str(err))

# Classe principal da aplicação que herda de customtkinter
class SistemaBancarioApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Bancário")

        self.banco = Banco()  

        # Criação do frame principal da aplicação
        self.frame_conta = ContaFrame(self)
        self.frame_conta.pack(expand=True, fill=ctk.BOTH)

# Classe para o frame que contém os elementos da interface relacionados à conta
class ContaFrame(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app  # Salva uma referência ao objeto SistemaBancarioApp
        self.conta_veri = False

        # Labels e entradas para inserir dados da conta e operações
        self.label_titular = ctk.CTkLabel(self, text="Titular da Conta:")
        self.label_titular.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.entrada_titular = ctk.CTkEntry(self)
        self.entrada_titular.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        self.botao_criar_conta = ctk.CTkButton(self, text="Criar Conta", command=self.criar_conta)
        self.botao_criar_conta.grid(row=1, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        self.label_operacoes = ctk.CTkLabel(self, text="Operações:")
        self.label_operacoes.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        self.entrada_deposito = ctk.CTkEntry(self)
        self.entrada_deposito.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

        self.botao_depositar = ctk.CTkButton(self, text="Depositar", command=self.depositar)
        self.botao_depositar.grid(row=3, column=1, padx=20, pady=5, sticky="ew")

        self.entrada_saque = ctk.CTkEntry(self)
        self.entrada_saque.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        self.botao_sacar = ctk.CTkButton(self, text="Sacar", command=self.sacar)
        self.botao_sacar.grid(row=4, column=1, padx=20, pady=5, sticky="ew")

        self.botao_ver_saldo = ctk.CTkButton(self, text="Ver Saldo", command=self.ver_saldo)
        self.botao_ver_saldo.grid(row=5, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        self.grid_columnconfigure(1, weight=1)

    # Método para criar uma conta bancária com base nos dados inseridos
    def criar_conta(self):
        titular = self.entrada_titular.get()
        if titular:
            conta = Conta(titular)
            self.app.banco.CriarConta(conta)
            self.conta_veri = True
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do titular da conta.")

    # Método para realizar um depósito na conta bancária
    def depositar(self):

        if self.conta_veri == True:
            nome = self.entrada_titular.get()
            valor = self.entrada_deposito.get()
        else:
            messagebox.showerror("aaaaaaaaaaaaaaa")

        if nome and valor:
            try:
                valor = float(valor)
                self.app.banco.Depositar(nome, valor)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um valor válido.")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do titular e o valor a ser depositado.")

    # Método para realizar um saque na conta bancária
    def sacar(self):
        nome = self.entrada_titular.get()
        valor = self.entrada_saque.get()
        if nome and valor:
            try:
                valor = float(valor)
                self.app.banco.Sacar(nome, valor)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um valor válido.")
            except SaldoInsuficiente:
                messagebox.showerror("Saldo Insuficiente", "Saldo insuficiente.")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do titular e o valor a ser sacado.")

    # Método para verificar o saldo da conta bancária
    def ver_saldo(self):
        nome = self.entrada_titular.get()
        if nome:
            self.app.banco.VerSaldo(nome)
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do titular.")

# Função principal que inicia a aplicação
if __name__ == "__main__":
    app = SistemaBancarioApp()
    app.mainloop()

