from banco_de_dados.db import Banco


class ClienteServices:
    def __init__(self):
        self.banco : Banco = Banco()


    def excluir(self, id):
        self.banco.deletar_cliente(id=id)


    def listar_clientes(self):
        return self.banco.listar_clientes()
