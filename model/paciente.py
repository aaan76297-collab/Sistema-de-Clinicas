from datetime import date
from .pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, identificador: int, nome: str, contato, cpf: str, data_nascimento: date):
        super().__init__(nome, contato, cpf)
        self.__identificador = identificador
        self.__data_nascimento = data_nascimento
        self.__historico_atendimentos = []

    @property
    def identificador(self):
        return self.__identificador

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self.__data_nascimento = valor

    @property
    def historico_atendimentos(self):
        return self.__historico_atendimentos.copy()

    def adicionar_atendimento(self, identificador_atendimento: int):
        self.__historico_atendimentos.append(identificador_atendimento)

    def idade(self, data_referencia: date = None) -> int:
        if data_referencia is None:
            data_referencia = date.today()
        idade_calculada = data_referencia.year - self.data_nascimento.year
        if (data_referencia.month, data_referencia.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade_calculada -= 1
        return idade_calculada

    def tipo(self) -> str:
        return "Paciente"

    def __str__(self):
        return (f"ID: {self.identificador} | Nome: {self.nome} | CPF: {self.cpf} | "
                f"Nasc: {self.data_nascimento.strftime('%d/%m/%Y')} | Contato: {self.contato}")