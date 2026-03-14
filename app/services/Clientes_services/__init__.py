from app.banco_de_dados.db import Banco
from app.models.Cliente import Cliente


class ClienteServices:
    def __init__(self):
        self.banco : Banco = Banco()


    def excluir(self, id):
        self.banco.deletar_cliente(id=id)


    def listar_clientes(self):
        return self.banco.listar_clientes()


    def cadastrar_cliente(self, cliente : Cliente):
        self.banco.cadastrar_cliente(cliente=cliente)
    

    def buscar_cliente(self, id):
        return self.banco.buscar_cliente_id(id)
    

    def atualizar_cliente(self, id, cliente_atualizado : Cliente):
        self.banco.atualizar_cadastro(id, cliente_atualizado)

    
    def buscar_cliente_email(self, email):
        return self.banco.buscar_cliente_email(email)
    
    def buscar_cliente_nome(self, nome):
        return self.banco.buscar_cliente_nome(nome)
    
    def buscar_cliente_id(self, id):
        return self.banco.buscar_cliente_id(id)
    