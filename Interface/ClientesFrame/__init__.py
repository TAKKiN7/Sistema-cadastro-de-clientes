from customtkinter import CTkFrame
from Interface.ClientesFrame.ClientesView import ClientesView


class ClientesFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="WHITE", corner_radius=20)
        self.layout()

    


    def layout(self):

        clientesLista : ClientesView = ClientesView(master=self)

        self.place(relx=.2, rely=.0, relwidth=.7, relheight=1)