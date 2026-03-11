from customtkinter import *
from Interface.ClientesView import ClientesView
from tkinter import messagebox as msg


class Janela(CTk):
    def __init__(self):
        super().__init__()
        self.config()
        self.layout() 
        self.run()


    def config(self):
        self.attributes("-fullscreen", True)
        self.title("Cadastro")
        self.configure(fg_color="#aaa")

    def layout(self):
        self.tabela_clientes : ClientesView = ClientesView(self)
        self.botoes_acao()



    def botoes_acao(self):
        adicionar_button : CTkButton = CTkButton(self, text="Novo Cadastro", fg_color="#ccc", text_color="BLACK", font=("itim", 12, "bold"), height=40, hover_color="#ccc",
        command=self.adicionar)
        remover_button : CTkButton = CTkButton(self, text="Excluir Cadastro", fg_color="#ccc", text_color="BLACK", font=("itim", 12, "bold"), height=40, hover_color="#ccc",
        command=self.remover)
        editar_button : CTkButton = CTkButton(self, text="Editar Cadastro", fg_color="#ccc", text_color="BLACK", font=("itim", 12, "bold"), height=40, hover_color="#ccc",
        command=self.editar)


        adicionar_button.bind("<Enter>", lambda e: self.enter_mouse(button=adicionar_button))
        editar_button.bind("<Enter>", lambda e: self.enter_mouse(button=editar_button))
        remover_button.bind("<Enter>", lambda e: self.enter_mouse(button=remover_button))

        adicionar_button.bind("<Leave>", lambda e: self.leave_mouse(button=adicionar_button))
        editar_button.bind("<Leave>", lambda e: self.leave_mouse(button=editar_button))
        remover_button.bind("<Leave>", lambda e: self.leave_mouse(button=remover_button))


        adicionar_button.place(relx=.856, rely=.02, relwidth=.04)
        editar_button.place(relx=.898, rely=.02, relwidth=.04)
        remover_button.place(relx=.94, rely=.02, relwidth=.04)


    def run(self):
        self.mainloop()


    def enter_mouse(self, button : CTkButton, e=None):
        button.configure(fg_color="#999", text_color="WHITE", hover_color="#999")


    def leave_mouse(self, button : CTkButton, e=None):
        button.configure(fg_color="#ccc", text_color="BLACK", hover_color="#ccc")


    def adicionar(self):
        msg.showinfo("Adicionar", "Adicionado com sucesso")

    
    def editar(self):
        msg.showinfo("Editar", "Editado com sucesso")


    def remover(self):
        selecionado = self.tabela_clientes.selection()
        if selecionado:
            valores = self.tabela_clientes.item(selecionado[0])
            id = valores.get("text")
            msg.showinfo("Remover", f"Cliente com ID:{id}. Removido com sucesso")
            self.tabela_clientes.selection_remove(self.tabela_clientes.selection())
