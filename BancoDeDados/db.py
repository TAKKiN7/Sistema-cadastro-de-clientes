import sqlite3
from pathlib import Path
from models.Cliente import Cliente

class Banco:
    def __init__(self):
        self.criar_banco()


    def criar_banco(self):
        try:
            local : Path = Path.cwd()
            banco : Path = Path("BancoDeDados")
            banco.touch(exist_ok=True)

            self.caminho : Path = Path(local / banco)
            self.caminho.touch(exist_ok=True)
        finally:
            with sqlite3.connect(self.caminho / "db.db") as conn:
                cursor : sqlite3.Cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), telefone VARCHAR(15), email VARCHAR(100), endereco TEXT, status VARCHAR(10))")


    def cadastrar_cliente(self, cliente : Cliente):    
        data : tuple = (cliente.nome, cliente.telefone, cliente.email, cliente.endereco, cliente.status)
        with sqlite3.connect(self.caminho / "db.db") as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes (nome, telefone, email, endereco, status) VALUES (?, ?, ?, ?, ?)", data)
            conn.commit()
    

    def deletar_cliente(self, id):
        with sqlite3.connect(self.caminho / "db.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (id, ))
            conn.commit()


    def buscar_cliente_id(self, id):
        with sqlite3.connect(self.caminho / "db.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = ?", (id, ))
            info = cursor.fetchone()

            if not info:
                return "Nenhum cliente com esse ID foi encontrado"

            dados : dict = dict(info)
            
            nome = dados.get("nome")
            telefone = dados.get("telefone")
            email = dados.get("email")
            endereco = dados.get("endereco")
            status = dados.get("status")
            id = dados.get("id")

            try:
                cliente : Cliente = Cliente(nome=nome, telefone=telefone, email=email, endereco=endereco, id=id, status=status)
            except:
                return "Erro ao tentar contruir o obj cliente"
            else:
                return cliente


    def desativar_cliente(self, id : int):
        data : tuple = ("INATIVO", id)
        with sqlite3.connect(self.caminho / "db.db") as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET status = ? WHERE id = ?", data)


    def ativar_cliente(self, id : int):
        data : tuple = ("ATIVO", id)
        with sqlite3.connect(self.caminho / "db.db") as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET status = ? WHERE id = ?", data)



    def alterar_nome(self, id : int ,novo_nome : str):
        data : tuple = (novo_nome, id)
        with sqlite3.connect(self.caminho / "db.db") as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", data)
            conn.commit()


    
    def listar_clientes(self) -> dict | str:
        with sqlite3.connect(self.caminho / "db.db") as conn:
            conn.row_factory = sqlite3.Row
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            res = cursor.fetchall()
            if not res:
                return "Nenhum cliente encontrado"
            
            return res


if __name__ == "__main__":
    banco : Banco = Banco()