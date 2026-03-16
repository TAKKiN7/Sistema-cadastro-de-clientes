from tkinter.ttk import Treeview, Style
from app.services.Clientes_services import ClienteServices
from tkinter import messagebox as msg

class ClientesView(Treeview):
    def __init__(self, master, fun_duplo_clique = None, filter : bool = False, nome : str = None, id : int = None, email : str = None):
        super().__init__(master)
        self.cliente_services : ClienteServices = ClienteServices()
        self.duplo_clique = fun_duplo_clique
        self.nome = nome.title() if nome else None
        self.id = id
        self.email = email.lower() if email else None
        self.filter = filter
        self.config_tree()
        self.layout()
    

    def config_tree(self):
        self["columns"] = ("nome", "telefone", "email", "endereco", "status")

        self.column("#0", width=100, stretch=False, anchor="w")
        self.column("nome")
        self.column("telefone")
        self.column("email")
        self.column("endereco")
        self.column("status", stretch=True, width=100, anchor="center")

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
        if not self.filter:
            self.inserir_clientes()
        elif self.nome:
            print("TO NO nome")
            self.inserir_clientes_nome(self.nome)
        elif self.id:
            print("TO NO ID")
            self.inserir_clientes_id(self.id)
        elif self.email:
            print("TO NO email")
            self.inserir_clientes_email(self.email)

        self.bind("<Double-1>", self.duplo_clique)
        self.place(relx=.02, rely=0.07, relheight=.9, relwidth=.96) 



    def inserir_clientes(self):
        clientes = self.cliente_services.listar_clientes()
        if not clientes:
            return
        for i, c in enumerate(clientes):
            cliente : dict = dict(c)
            
            # sequencia dos valores id, nome, telefone, email, endereco, status
            id = cliente.get("id")

            ativo = cliente.get("status").lower() == "ativo"
            if not ativo:
                valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"INATIVO")
            else:   
                valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"ATIVO")


            if i % 2 == 0:
                self.insert("", "end", text= id, values=valores, tags=("linha1", ))
            else:
                self.insert("", "end", text= id, values=valores, tags=("linha2", ))



    def inserir_clientes_nome(self, nome : str):
        clientes = self.cliente_services.buscar_cliente_nome(nome=nome)
        if not clientes:
            msg.showinfo("","Nenhum cadastro encontrado")
            return
        for i, cliente in enumerate(clientes):
            #cliente : dict = dict(c)
            
            # sequencia dos valores id, nome, telefone, email, endereco, status
            id = cliente.get("id")

            ativo = cliente.get("status").lower() == "ativo"
            if not ativo:
                valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"INATIVO")
            else:   
                valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"ATIVO")


            if i % 2 == 0:
                self.insert("", "end", text= id, values=valores, tags=("linha1", ))
            else:
                self.insert("", "end", text= id, values=valores, tags=("linha2", ))

    
    def inserir_clientes_id(self, id : int):
        cliente = self.cliente_services.buscar_cliente(id=id)
        if not cliente:
            msg.showinfo("","Nenhum cadastro encontrado")
            return
        
        id = cliente.id

        ativo = cliente.status.lower() == "ativo"
        if not ativo:
            valores : tuple = (cliente.nome, cliente.telefone, cliente.email, cliente.endereco, cliente.status.upper())
        else:   
            valores : tuple = (cliente.nome, cliente.telefone, cliente.email, cliente.endereco, cliente.status.upper())

        self.insert("", "end", text= id, values=valores, tags=("linha1", ))


    def inserir_clientes_email(self, email : str):
        res = self.cliente_services.buscar_cliente_email(email)
        if not res:
            msg.showinfo("","Nenhum cadastro encontrado")
            return
        
        cliente : dict = dict(res)

        id = cliente.get("id")

        ativo = cliente.get("status").lower() == "ativo"
        if not ativo:
            valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"INATIVO")
        else:   
            valores : tuple = (cliente.get("nome"), cliente.get("telefone"), cliente.get("email"), cliente.get("endereco"), f"ATIVO")

        self.insert("", "end", text= id, values=valores, tags=("linha1", ))


    def estilo(self):
        style : Style = Style()
        style.configure("Treeview.Heading", font=("Verdana", 15, "bold"))

        # No linux para esses emojis "🔴 🟢 🟡" aparecer tem que deixar essa font= "Noto Color Emoji"
        style.configure("Treeview", font=("Verdana", 13), rowheight=30)