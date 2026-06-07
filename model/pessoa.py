import abc

class Pessoa(abc.ABC):
    def __init__(self, nome: str, contato, cpf: str):
        self.__nome = nome
        self.__contato = contato
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, valor):
        self.__contato = valor

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    @abc.abstractmethod
    def tipo(self) -> str:
        pass