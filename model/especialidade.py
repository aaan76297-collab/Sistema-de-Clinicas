class Especialidade:
    def __init__(self, identificador: int, nome: str, descricao: str):
        self.__identificador = identificador
        self.__nome = nome
        self.__descricao = descricao

    @property
    def identificador(self):
        return self.__identificador

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    def __str__(self):
        return f"ID: {self.identificador} | Nome: {self.nome} | Descrição: {self.descricao}"