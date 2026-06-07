class Contato:
    def __init__(self, telefone: str, email: str):
        self.__telefone = telefone
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    def __str__(self):
        return f"Tel: {self.telefone} | E-mail: {self.email}"