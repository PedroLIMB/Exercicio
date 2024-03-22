import sqlite3
import customtkinter

class Conta():
    def __init__(self, nome, saldo): 
        self.nome = nome 
        self.saldo = saldo

class Banco():
    def __init__(self):
        self.banco = sqlite3.connect("bancoDosMano.db")
        self.cursor = self.banco.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS banco (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(80), saldo INTEGER)''')

        self.banco.commit()
        self.banco.close()

    def CriarConta(self, conta): 
        self.conta = conta
        
        self.banco = sqlite3.connect("bancoDosMano.db")
        self.cursor = self.banco.cursor()

        try:

            if not isinstance(self.conta.saldo, (int, float)) or not isinstance(self.conta.nome, (str)):
                print("nome ou saldo errados")
        
            else:
                self.cursor.execute("INSERT INTO banco (nome, saldo) VALUES (?, ?)", (self.conta.nome, self.conta.saldo,))

                showDatabase = self.cursor.execute("SELECT * FROM banco").fetchall()
                print(showDatabase)

                self.banco.commit()

        except sqlite3.Error as err:
            print("erro ao criar conta")
        finally:
            self.banco.close()

    def Depositar(self, valor): 
        self.valor = valor

        self.banco = sqlite3.connect("bancoDosMano.db")
        self.cursor = self.banco.cursor()

        try:

            self.cursor.execute("UPDATE banco SET saldo = saldo + ? where nome = ?", (self.valor, self.conta.nome))
            showDatabase = self.cursor.execute("SELECT * FROM banco").fetchall()
            print(showDatabase)

            self.banco.commit()

        except sqlite3.Error as err:
            print("erro ao depositar")
        finally: 
            self.banco.close()

    def Sacar(self, valor): 
        self.valor = valor

        self.banco = sqlite3.connect("bancoDosMano.db")
        self.cursor = self.banco.cursor()

        try:

            self.cursor.execute("UPDATE banco SET saldo = saldo - ? where nome = ?", (self.valor, self.conta.nome))
            showDatabase = self.cursor.execute("SELECT * FROM banco").fetchall()
            print(showDatabase)
            self.banco.commit()

        except sqlite3.Error as err:
            print("erro ao sacar")
        finally:
            self.banco.close()

class Janela():
    pass

if __name__ == "__main__":
    banco = Banco()
    
    conta01 = Conta("nome", "aaaaaa")

    banco.CriarConta(conta01)

    # janela = customtkinter.CTk()
    # janela.geometry("700x400")
    # janela.resizable(width=False, height=False)
    # janela._set_appearance_mode("dark")
    # janela.title("Banco UDI")



    
 

    # janela.mainloop()

    

