from customtkinter import CTkToplevel



class CadastroCliente(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.config()
        self.focar() # para uso no Linux
        #self.grab_set() Para uso no windows

    def config(self):
        self.title("Novo Cadastro")
    
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        largura_janela = 800
        altura_janela = 500

        self.geometry(f"{largura_janela}x{altura_janela}+{int((largura_tela / 2 ) - (largura_janela / 2))}+{int((altura_tela / 2) - (altura_janela / 2))}")
        self.maxsize(800, 500)
        self.minsize(800, 500)


    def focar(self):
        self.after(10, self.grab_set)
        self.focus()


    def layout(self):
        pass