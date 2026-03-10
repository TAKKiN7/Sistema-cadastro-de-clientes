from customtkinter import *
from Interface.ClientesFrame import ClientesFrame
from Interface.ClientesFrame.ClientesView import ClientesView

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

        #clientesF : CTkFrame = ClientesFrame(self)

    
    def run(self):
        self.mainloop()
