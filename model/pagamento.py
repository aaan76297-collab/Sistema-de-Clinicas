import abc
from datetime import date, time

class Pagamento(abc.ABC):
    def __init__(self, identificador: int, data_pagamento: date, hora: time, valor: float):
        self.__identificador = identificador
        self.__data_pagamento = data_pagamento
        self.__hora = hora
        self.__valor = valor

    @property
    def identificador(self):
        return self.__identificador

    @property
    def data_pagamento(self):
        return self.__data_pagamento

    @property
    def hora(self):
        return self.__hora

    @property
    def valor(self):
        return self.__valor

    @abc.abstractmethod
    def modalidade(self) -> str:
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class PagamentoDinheiro(Pagamento):
    def __init__(self, identificador: int, data_pagamento: date, hora: time, valor: float):
        super().__init__(identificador, data_pagamento, hora, valor)

    def modalidade(self) -> str:
        return "Dinheiro"

    def __str__(self):
        return (f"ID: {self.identificador} | Dinheiro | Data: {self.data_pagamento.strftime('%d/%m/%Y')} "
                f"Hora: {self.hora.strftime('%H:%M')} | Valor: R$ {self.valor:.2f}")


class PagamentoPix(Pagamento):
    def __init__(self, identificador: int, data_pagamento: date, hora: time, valor: float,
                 nome_pagador: str, tipo_pessoa: str, documento: str):
        super().__init__(identificador, data_pagamento, hora, valor)
        self.__nome_pagador = nome_pagador
        self.__tipo_pessoa = tipo_pessoa
        self.__documento = documento

    @property
    def nome_pagador(self):
        return self.__nome_pagador

    @property
    def tipo_pessoa(self):
        return self.__tipo_pessoa

    @property
    def documento(self):
        return self.__documento

    def modalidade(self) -> str:
        return "PIX"

    def __str__(self):
        return (f"ID: {self.identificador} | PIX | Data: {self.data_pagamento.strftime('%d/%m/%Y')} "
                f"Hora: {self.hora.strftime('%H:%M')} | Valor: R$ {self.valor:.2f} | "
                f"Pagador: {self.nome_pagador} ({self.documento})")


class PagamentoCartao(Pagamento):
    MODALIDADES = ["credito", "debito"]

    def __init__(self, identificador: int, data_pagamento: date, hora: time, valor: float,
                 tipo_cartao: str, numero_cartao: str, modalidade_cartao: str, numero_parcelas: int):
        super().__init__(identificador, data_pagamento, hora, valor)
        self.__tipo_cartao = tipo_cartao
        self.__numero_cartao = numero_cartao
        self.__modalidade_cartao = modalidade_cartao
        self.__numero_parcelas = numero_parcelas

    @property
    def tipo_cartao(self):
        return self.__tipo_cartao

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def modalidade_cartao(self):
        return self.__modalidade_cartao

    @property
    def numero_parcelas(self):
        return self.__numero_parcelas

    def modalidade(self) -> str:
        return "Cartão"

    def __str__(self):
        return (f"ID: {self.identificador} | Cartão {self.tipo_cartao} | Data: {self.data_pagamento.strftime('%d/%m/%Y')} "
                f"Hora: {self.hora.strftime('%H:%M')} | Valor: R$ {self.valor:.2f} | "
                f"{self.modalidade_cartao} | Parcelas: {self.numero_parcelas}")