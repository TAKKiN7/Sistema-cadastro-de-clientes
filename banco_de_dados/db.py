import sqlite3
from pathlib import Path
from models.Cliente import Cliente

class Banco:
    def __init__(self):
        self.criar_banco()


    def criar_banco(self):
        try:
            self.caminho : Path = Path.cwd() / "banco_de_dados"
            self.caminho.mkdir(exist_ok=True)
        finally:
            with self.banco_conn() as conn:
                cursor : sqlite3.Cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), telefone VARCHAR(15), email VARCHAR(100), endereco TEXT, status VARCHAR(10))")


    def banco_conn(self):
        self.db = self.caminho / "db.db"
        conn : sqlite3.Connection = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        return conn
    

    def cadastrar_cliente(self, cliente : Cliente):    
        data : tuple = (cliente.nome, cliente.telefone, cliente.email, cliente.endereco, cliente.status)
        with self.banco_conn() as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes (nome, telefone, email, endereco, status) VALUES (?, ?, ?, ?, ?)", data)
            conn.commit()
    

    def deletar_cliente(self, id):
        with self.banco_conn() as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (id, ))
            conn.commit()


    def buscar_cliente_id(self, id):
        with self.banco_conn() as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = ?", (id, ))
            info = cursor.fetchone()

            if not info:
                return

            dados : dict = dict(info)
            
            nome = dados.get("nome")
            telefone = dados.get("telefone")
            email = dados.get("email")
            endereco = dados.get("endereco")
            status = dados.get("status")
            id = dados.get("id")

            try:
                cliente : Cliente = Cliente(nome=nome, telefone=telefone, email=email, endereco=endereco, id=id, status=status)
            except Exception as e:
                return f"Erro ao tentar construir o obj cliente. Erro: {e}"
            else:
                return cliente


    def desativar_cliente(self, id : int):
        data : tuple = ("INATIVO", id)
        with self.banco_conn() as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET status = ? WHERE id = ?", data)
            conn.commit()


    def ativar_cliente(self, id : int):
        data : tuple = ("ATIVO", id)
        with self.banco_conn() as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET status = ? WHERE id = ?", data)
            conn.commit()


    def alterar_nome(self, id : int ,novo_nome : str):
        data : tuple = (novo_nome, id)
        with self.banco_conn() as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", data)
            conn.commit()


    
    def listar_clientes(self) -> dict | str:
        with self.banco_conn() as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            res = cursor.fetchall()
            if not res:
                return "Nenhum cliente encontrado"
            
            return res


if __name__ == "__main__":
    banco : Banco = Banco()