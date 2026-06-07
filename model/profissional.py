from datetime import time
from .pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, identificador: int, nome: str, contato, cpf: str,
                 registro_profissional: str, especialidade_identificador: int,
                 dias_trabalho: list, horario_inicio: time, horario_fim: time):
        super().__init__(nome, contato, cpf)
        self.__identificador = identificador
        self.__registro_profissional = registro_profissional
        self.__especialidade_identificador = especialidade_identificador
        self.__dias_trabalho = dias_trabalho
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__clinicas_associadas = []
        self.__historico_atendimentos = []

    @property
    def identificador(self):
        return self.__identificador

    @property
    def registro_profissional(self):
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, valor):
        self.__registro_profissional = valor

    @property
    def especialidade_identificador(self):
        return self.__especialidade_identificador

    @especialidade_identificador.setter
    def especialidade_identificador(self, valor):
        self.__especialidade_identificador = valor

    @property
    def dias_trabalho(self):
        return self.__dias_trabalho.copy()

    @dias_trabalho.setter
    def dias_trabalho(self, valor):
        self.__dias_trabalho = valor

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, valor):
        self.__horario_inicio = valor

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, valor):
        self.__horario_fim = valor

    @property
    def clinicas_associadas(self):
        return self.__clinicas_associadas.copy()

    def adicionar_clinica(self, identificador_clinica: int):
        self.__clinicas_associadas.append(identificador_clinica)

    @property
    def historico_atendimentos(self):
        return self.__historico_atendimentos.copy()

    def adicionar_atendimento(self, identificador_atendimento: int):
        self.__historico_atendimentos.append(identificador_atendimento)

    def tipo(self) -> str:
        return "Profissional"

    def __str__(self):
        return (f"ID: {self.identificador} | Nome: {self.nome} | Registro: {self.registro_profissional} | "
                f"CPF: {self.cpf} | Especialidade ID: {self.especialidade_identificador} | Contato: {self.contato}")