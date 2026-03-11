from BancoDeDados.db import Banco
from models.Cliente import Cliente
from Interface import Janela


# Criação da conexão com o banco de dados
banco : Banco = Banco()


# Criação de um obj clientes com as informações reais do cliente
# cliente : Cliente = Cliente("Lucas", "4444-4444", "lucas@gmail.com", "Rua Joao de Barro, 53, Macuco, Timóteo")



# Passar o obj cliente para o banco para ele adicionar no banco de dados
# banco.cadastrar_cliente(cliente)


# for c in range(0, 100, 2):
#     banco.desativar_cliente(c)


# buscar um cliente no banco de dados pelo ID
# cliente : Cliente = banco.buscar_cliente_id(2)


# Atualizar o nome pelo id 
# banco.alterar_nome(2, "JKSDJAD")

# listar todos os clientes do banco de dados

# clientes = banco.listar_clientes()

# if clientes:
#     for c in clientes:
#         cliente : dict = dict(c)
#         print(cliente)



# Inicializar a janela de interface Grafica

janela : Janela = Janela()