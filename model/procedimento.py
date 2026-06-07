class Procedimento:
    def __init__(self, identificador: int, descricao: str, duracao: int, preco: float):
        self.__identificador = identificador
        self.__descricao = descricao
        self.__duracao = duracao
        self.__preco = preco

    @property
    def identificador(self):
        return self.__identificador

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, valor):
        self.__duracao = valor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        self.__preco = valor

    def __str__(self):
        return (f"ID: {self.identificador} | Descrição: {self.descricao} | "
                f"Duração: {self.duracao} min | Preço: R$ {self.preco:.2f}")