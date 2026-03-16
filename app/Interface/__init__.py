from customtkinter import *
from app.Interface.ClientesView import ClientesView
from tkinter import messagebox as msg
from app.services.Clientes_services import ClienteServices
from app.Interface.CadastroCliente import CadastroCliente
from app.models.Cliente import Cliente
from app.Interface.EditarCliente import EditarCliente


class Janela(CTk):
    def __init__(self):
        super().__init__()
        self.cliente_services : ClienteServices = ClienteServices()
        self.config()
        self.layout() 
        self.run()


    def config(self):
        self.attributes("-fullscreen", True)
        self.geometry("1920x1080")
        self.title("Cadastro")
        self.configure(fg_color="#ccc")

    def layout(self):
        self.frame_fundo()
        self.tabela_clientes : ClientesView = ClientesView(self, fun_duplo_clique=self.editar)
        self.botoes_acao()



    def botoes_acao(self):
        tamanho_tela : int = self.winfo_screenheight()
        print(tamanho_tela)
        if tamanho_tela == 1080:
            tamanho_letra = 12
            tamanho_letra_fechar = 15
        else:
            tamanho_letra = 17
            tamanho_letra_fechar = 17

        
        # Area dos Botoes de acao
        adicionar_button : CTkButton = CTkButton(self, text="Novo Cadastro", fg_color="#ccc", text_color="BLACK", corner_radius=0, font=("arial", tamanho_letra, "bold"), height=40, hover_color="#ccc",
        command=self.adicionar, border_width=2,  border_color="#888")
        remover_button : CTkButton = CTkButton(self, text="Excluir Cadastro", fg_color="#ccc", text_color="BLACK", corner_radius=0, font=("arial", tamanho_letra, "bold"), height=40, hover_color="#ccc",
        command=self.remover, border_width=2,  border_color="#888")
        editar_button : CTkButton = CTkButton(self, text="Editar Cadastro", fg_color="#ccc", text_color="BLACK", corner_radius=0, font=("arial", tamanho_letra, "bold"), height=40, hover_color="#ccc",
        command=self.editar, border_width=2,  border_color="#888")
        atualizar_button : CTkButton = CTkButton(self, text="Atualizar", fg_color="#ccc", text_color="BLACK", corner_radius=0, font=("arial", tamanho_letra, "bold"), height=40, hover_color="#ccc",
        command=self.atualizar, border_width=2,  border_color="#888")
        sair_button : CTkButton = CTkButton(self, text="Sair", fg_color="#ad1f2f", text_color="BLACK", corner_radius=0, font=("arial", tamanho_letra_fechar, "bold"), height=40, hover_color="#821723",
        command=self.fechar, border_width=2,  border_color="#888")


        adicionar_button.bind("<Enter>", lambda e: self.enter_mouse(button=adicionar_button))
        editar_button.bind("<Enter>", lambda e: self.enter_mouse(button=editar_button))
        remover_button.bind("<Enter>", lambda e: self.enter_mouse(button=remover_button))
        atualizar_button.bind("<Enter>", lambda e: self.enter_mouse(button=atualizar_button))


        adicionar_button.bind("<Leave>", lambda e: self.leave_mouse(button=adicionar_button))
        editar_button.bind("<Leave>", lambda e: self.leave_mouse(button=editar_button))
        remover_button.bind("<Leave>", lambda e: self.leave_mouse(button=remover_button))
        atualizar_button.bind("<Leave>", lambda e: self.leave_mouse(button=atualizar_button))


        adicionar_button.place(relx=.072, rely=.02, relwidth=.05)
        editar_button.place(relx=.124, rely=.02, relwidth=.05)
        remover_button.place(relx=.176, rely=.02, relwidth=.055)
        atualizar_button.place(relx=0.02, rely=.02, relwidth=.05)
        sair_button.place(relx=0.93, rely=.02, relwidth=.05)


        # Area de pesquisa
        pesquisaE : CTkEntry = CTkEntry(self, font=("arial", tamanho_letra + 5, "bold"), corner_radius=0, bg_color="#ccc")
        pesquisa_button : CTkButton = CTkButton(self, text="Buscar", fg_color="#ccc", text_color="BLACK", corner_radius=0, font=("arial", tamanho_letra, "bold"), height=40, hover_color="#ccc", command=lambda: self.pesquisa(valor=pesquisaE.get(), opcao=opcoes_CB.get()), border_width=2,  border_color="#888")


        opcoes : list = ["ID", "Nome", "Email"]
        opcoes_CB : CTkComboBox = CTkComboBox(self, values=opcoes, fg_color="#ccc", border_color="#888", bg_color="#aaa",
                                              text_color="BLACK", button_color="#888")

        pesquisaE.bind("<Return>", lambda e: self.pesquisa(valor=pesquisaE.get(), opcao=opcoes_CB.get()))

        pesquisa_button.bind("<Enter>", lambda e: self.enter_mouse(button=pesquisa_button))
        pesquisa_button.bind("<Leave>", lambda e: self.leave_mouse(button=pesquisa_button))

        pesquisaE.place(relx=.42, rely=.02, relwidth=.16, relheight=.0375)
        pesquisa_button.place(relx=.582, rely=.02, relwidth=.05)
        opcoes_CB.place(relx=.64, rely=.025, relheight=.03, relwidth=.07)


    def run(self):
        self.mainloop()


    def enter_mouse(self, button : CTkButton, e=None):
        button.configure(fg_color="#999", text_color="WHITE", hover_color="#999")


    def leave_mouse(self, button : CTkButton, e=None):
        button.configure(fg_color="#ccc", text_color="BLACK", hover_color="#ccc")


    def atualizar(self):
        self.atualizar_tabela_clientes()

    def adicionar(self):
        # msg.showinfo("Adicionar", "Adicionado com sucesso")
        janela_novo_cadastro : CadastroCliente = CadastroCliente(self, fun_atualizar_tabela=self.atualizar_tabela_clientes)

    
    def editar(self, e=None):
        selecionado = self.tabela_clientes.selection()
        if not selecionado:
            msg.showinfo("Error", "Nenhum cadastro selecionado")
            return
        

        id = self.tabela_clientes.item(selecionado[0]).get("text")

        print(id)

        cliente : Cliente = self.cliente_services.buscar_cliente(id)

        janela_editar_cliente : EditarCliente = EditarCliente(self, cliente=cliente, fun_atualizar_tabela=self.atualizar_tabela_clientes)

        #self.tabela_clientes.selection_remove(self.tabela_clientes.selection())

    def remover(self):
        selecionado = self.tabela_clientes.selection()
        if not selecionado:
            msg.showinfo("Error", "Nenhum cadastro selecionado")
            return
        
        valores = self.tabela_clientes.item(selecionado[0])
        
        nome : str = valores.get("values")[0]

        res = msg.askyesno("Confirme", f"Excluir {nome}")
        if not res:
            return
        
        
        id = valores.get("text")

        self.cliente_services.excluir(id)

        if len(selecionado) > 1:
            msg.showinfo("Feito", f"Clientes removidos com sucesso.")
        else:
            msg.showinfo("Feito", f"Cliente removido com sucesso.")
        self.tabela_clientes.selection_remove(self.tabela_clientes.selection())
        self.atualizar_tabela_clientes()


    def atualizar_tabela_clientes(self):
        self.tabela_clientes.place_forget()
        self.tabela_clientes : ClientesView = ClientesView(self, fun_duplo_clique=self.editar)

    
    def pesquisa(self, valor : str, opcao, e=None):
        self.tabela_clientes.place_forget()

        match opcao.lower():
            case "id":
                self.tabela_clientes : ClientesView = ClientesView(self, fun_duplo_clique=self.editar, filter= True, id=int(valor))
            case "nome":
                self.tabela_clientes : ClientesView = ClientesView(self, fun_duplo_clique=self.editar, filter= True, nome=valor.strip())
            case "email":
                self.tabela_clientes : ClientesView = ClientesView(self, fun_duplo_clique=self.editar, filter= True, email=valor.strip())


    def fechar(self):
        self.destroy()

    def frame_fundo(self):
        frame : CTkFrame = CTkFrame(self, fg_color="#aaa", bg_color="#ccc", corner_radius=20, border_width=3, border_color="#000")
        frame.place(relx=.01, rely=.01, relwidth=.98, relheight=.98)