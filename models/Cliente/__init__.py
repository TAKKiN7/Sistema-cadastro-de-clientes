class Cliente:
    def __init__(self, nome : str, telefone : str, email : str, endereco : str, id : int = None, status : str = "ATIVO"):
        self._id = id
        self._nome = nome.strip()
        self._telefone = telefone.strip()
        self._email = email.strip()
        self._endereco = endereco.strip()
        self._status = status

    
    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return self._status
    
    @property
    def nome(self):
        return self._nome
 
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def email(self):
        return self._email
    
    @property
    def endereco(self):
        return self._endereco

    def alterar_email(self, novo_email):
        self._nome = novo_email


    def alterar_telefone(self, novo_telefone):
        self._nome = novo_telefone
       

    def alterar_nome(self, novo_nome : str):
        self._nome = novo_nome
    

    def alterar_endereco(self, novo_endereco):
        self._endereco = novo_endereco


if __name__ == "__main__":
    cliente : Cliente = Cliente("Lucas", "4444-4444", "lucas@gmail.com")

    print(cliente.nome)
    cliente.alterar_nome("Marcos")
    print(cliente.nome)
    print(cliente.email)
    print(cliente.telefone)
    print(cliente.id)