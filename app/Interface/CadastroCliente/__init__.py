from customtkinter import CTkToplevel, CTkButton, CTkLabel, CTkEntry
from tkinter import messagebox as msg
from app.models.Cliente import Cliente
from app.services.Clientes_services import ClienteServices
import re


class CadastroCliente(CTkToplevel):
    def __init__(self, master, fun_atualizar_tabela):
        super().__init__(master)
        self.service_cliente : ClienteServices = ClienteServices()
        self.fun_atualizar_tabela = fun_atualizar_tabela
        self.config()
        self.layout()
        self.focar() # para uso no Linux
        #self.grab_set() Para uso no windows

    def config(self):

        self.configure(fg_color="#aaa")

        self.title("Novo Cadastro")
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        largura_janela = 800
        altura_janela = 300

        self.geometry(f"{largura_janela}x{altura_janela}+{int((largura_tela / 2 ) - (largura_janela / 2))}+{int((altura_tela / 2) - (altura_janela / 2))}")
        self.maxsize(800, 300)
        self.minsize(800, 300)


    def focar(self):
        self.after(10, self.grab_set)
        self.focus()


    def layout(self):

        nomeL : CTkLabel = CTkLabel(self, text="Nome:", fg_color="#aaa", corner_radius=0, bg_color="#aaa", text_color="BLACK")
        telefoneL : CTkLabel = CTkLabel(self, text="Telefone:", fg_color="#aaa", corner_radius=0, bg_color="#aaa", text_color="BLACK")
        emailL : CTkLabel = CTkLabel(self, text="Email:", fg_color="#aaa", corner_radius=0, bg_color="#aaa", text_color="BLACK")
        enderecoL : CTkLabel = CTkLabel(self, text="Endereco:", fg_color="#aaa", corner_radius=0, bg_color="#aaa", text_color="BLACK")

        self.nomeE : CTkEntry = CTkEntry(self, fg_color="#ccc", text_color="BLACK", font=("arial", 13))
        self.telefoneE : CTkEntry = CTkEntry(self, fg_color="#ccc", text_color="BLACK", font=("arial", 13))
        self.emailE : CTkEntry = CTkEntry(self, fg_color="#ccc", text_color="BLACK", font=("arial", 13))
        self.enderecoE : CTkEntry = CTkEntry(self, fg_color="#ccc", text_color="BLACK", font=("arial", 13))


        self.nomeE.bind("<Return>", lambda event: self.confirmar())
        self.telefoneE.bind("<Return>", lambda event: self.confirmar())
        self.emailE.bind("<Return>", lambda event: self.confirmar())
        self.enderecoE.bind("<Return>", lambda event: self.confirmar())


        nomeL.place(relx=.013, rely=.1, relwidth=.1)
        emailL.place(relx=.49, rely=.1, relwidth=.1)
        telefoneL.place(relx=.02, rely=.23, relwidth=.1)        
        enderecoL.place(relx=.34, rely=.23, relwidth=.1)        
        
        self.nomeE.place(relx=.1, rely=.1, relwidth=.38)
        self.emailE.place(relx=.57, rely=.1, relwidth=.38)
        self.telefoneE.place(relx=.11, rely=.23, relwidth=.22)
        self.enderecoE.place(relx=.43, rely=.23, relwidth=.52)

        self.after(10, self.nomeE.focus)



        self.bototes_acao()


    def bototes_acao(self):
        cancelar_button : CTkButton = CTkButton(self, text_color="BLACK", corner_radius=0, border_width=2, border_color="#888", fg_color="#ccc", hover_color="#ccc", font=("arial", 13), text="Cancelar",command=self.cancelar)
        confirmar_button : CTkButton = CTkButton(self, text_color="BLACK", corner_radius=0, border_width=2, border_color="#888", fg_color="#ccc", hover_color="#ccc", font=("arial", 13), text="Confirmar", command=self.confirmar)


        cancelar_button.bind("<Enter>", lambda e: self.enter_mouse(button=cancelar_button))
        confirmar_button.bind("<Enter>", lambda e: self.enter_mouse(button=confirmar_button))

        cancelar_button.bind("<Leave>", lambda e: self.leave_mouse(button=cancelar_button))
        confirmar_button.bind("<Leave>", lambda e: self.leave_mouse(button=confirmar_button))

        cancelar_button.place(relx=.2, rely=.8)
        confirmar_button.place(relx=.5, rely=.8)

    
    def enter_mouse(self, button : CTkButton, e=None):
        button.configure(fg_color="#999", text_color="WHITE", hover_color="#999")


    def leave_mouse(self, button : CTkButton, e=None):
        button.configure(fg_color="#ccc", text_color="BLACK", hover_color="#ccc")


    def confirmar(self, event=None):
        dados : dict = self.leitura_de_dados()
        if not dados:
            return
    
        cliente : Cliente = Cliente(dados.get("nome"), dados.get("telefone"), dados.get("email").lower(), dados.get("endereco"))      
        
        self.service_cliente.cadastrar_cliente(cliente=cliente)
        
        self.fun_atualizar_tabela()
        self.fechar()


    def leitura_de_dados(self):
        if not self.nomeE.get().strip():
            msg.showerror("Campo incorreto", "*Nome* Campo obrigatorio esta Vazio")
            return
        elif not self.emailE.get().strip():
            msg.showerror("Campo incorreto", "*Email* Campo obrigatorio esta Vazio")
            return
        elif not self.telefoneE.get().strip():
            msg.showerror("Campo incorreto", "*Telefone* Campo obrigatorio esta Vazio")
            return
        elif not self.enderecoE.get().strip():
            msg.showerror("Campo incorreto", "*Endereco* Campo obrigatorio esta Vazio")
            return
        
        if not self.validar_email(self.emailE.get().strip().lower()):
            msg.showerror("Erro", "Email invalido")
            return

        cliente = self.service_cliente.buscar_cliente_email(self.emailE.get().strip().lower())
        if cliente:
            msg.showerror("Erro", "Email ja cadastrado para outro cliente")
            return

        if not self.validar_telefone(self.telefoneE.get().lower().strip()):
            msg.showerror("Erro", "Telefone invalido")
            return    

        dados : dict = {
            "nome" : self.nomeE.get().strip().title(),
            "email" : self.emailE.get().strip().lower(),
            "telefone" : self.telefoneE.get().strip().lower().replace(" ", "").replace("-", ""),
            "endereco" : self.enderecoE.get().strip().title()
        }

        return dados


    

    def validar_email(self, email: str) -> bool:
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(padrao, email) is not None

    def validar_telefone(self, telefone: str) -> bool:
        padrao = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
        return re.match(padrao, telefone) is not None


        
    def cancelar(self):
        self.fechar()


    def fechar(self):
        self.destroy()