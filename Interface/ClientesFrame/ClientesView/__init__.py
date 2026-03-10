from tkinter.ttk import Treeview, Style
from BancoDeDados.db import Banco


class ClientesView(Treeview):
    def __init__(self, master):
        super().__init__(master)
        self.banco : Banco = Banco()
        self.config_tree()
        self.layout()
    

    def config_tree(self):
        self["columns"] = ("nome", "telefone", "email", "endereco", "status")

        self.column("#0", width=50, stretch=False)
        self.column("nome")
        self.column("telefone", width=200, stretch=False)
        self.column("email")
        self.column("endereco")
        self.column("status", stretch=False, width=100, anchor="center")

        self.heading("#0", text="ID", anchor="center") 
        self.heading("nome", text="Nome") 
        self.heading("telefone", text="Telefone")
        self.heading("email", text="Email")
        self.heading("endereco", text="Endereco")
        self.heading("status", text="Status")


        self.tag_configure("linha1", background="#aaa")
        self.tag_configure("linha2", background="#ccc")

        self.estilo()

    def layout(self):   
        self.inserir_clientes()

        self.place(relx=.02, rely=0.02, relheight=.9, relwidth=.96) 



    def inserir_clientes(self):
        clientes = self.banco.listar_clientes()
        if clientes == "Nenhum cliente encontrado":
            return
        for i, c in enumerate(clientes):
            cliente : dict = dict(c)
            
            # sequencia dos valores id, nome, telefone, email, endereco, status
            id = cliente.get("id")

            ativo = cliente.get("status").lower() == "ativo"
            if not ativo:
                valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"🔴")
            else:   
                valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"🔵") # caso for necessario um status pendente 🔶


            if i % 2 == 0:
                self.insert("", "end", text= id, values=valores, tags=("linha1", ))
            else:
                self.insert("", "end", text= id, values=valores, tags=("linha2", ))


    def estilo(self):
        style : Style = Style()
        style.configure("Treeview.Heading", font=("Verdana", 15))

        # No linux para esses emojis "🔴 🟢 🟡" aparecer tem que deixar essa font= "Noto Color Emoji"
        style.configure("Treeview", font=("Verdana", 13), rowheight=30)