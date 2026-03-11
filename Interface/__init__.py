from customtkinter import *
from Interface.ClientesView import ClientesView

class Janela(CTk):
    def __init__(self):
        super().__init__()
        self.config()
        self.layout()

        
        
        self.run()


    def config(self):
        self.attributes("-fullscreen", True)
        

    def layout(self):
        tabela_clientes : ClientesView = ClientesView(self)


    
    def run(self):
        self.mainloop()
