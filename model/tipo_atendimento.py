class TipoAtendimento:
    def __init__(self, identificador: int, nome: str, descricao: str, duracao_maxima: int):
        self.__identificador = identificador
        self.__nome = nome
        self.__descricao = descricao
        self.__duracao_maxima = duracao_maxima

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

    @property
    def duracao_maxima(self):
        return self.__duracao_maxima

    @duracao_maxima.setter
    def duracao_maxima(self, valor):
        self.__duracao_maxima = valor

    def __str__(self):
        return (f"ID: {self.identificador} | Nome: {self.nome} | Descrição: {self.descricao} | "
                f"Duração máx.: {self.duracao_maxima} min")