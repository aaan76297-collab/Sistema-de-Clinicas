from datetime import time
from .contato import Contato

class Clinica:
    def __init__(self, identificador: int, nome: str, localizacao: str, descricao: str,
                 horario_abertura: time, horario_fechamento: time,
                 dias_funcionamento: list, contato: Contato):
        self.__identificador = identificador
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__dias_funcionamento = dias_funcionamento
        self.__contato = contato
        self.__tipos_atendimento = []   # IDs
        self.__profissionais = []       # IDs
        self.__pacientes = []           # IDs
        self.__atendimentos = []        # IDs

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
    def localizacao(self):
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, valor):
        self.__localizacao = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, valor):
        self.__horario_abertura = valor

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, valor):
        self.__horario_fechamento = valor

    @property
    def dias_funcionamento(self):
        return self.__dias_funcionamento.copy()

    @dias_funcionamento.setter
    def dias_funcionamento(self, valor):
        self.__dias_funcionamento = valor

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, valor):
        self.__contato = valor

    @property
    def tipos_atendimento(self):
        return self.__tipos_atendimento.copy()

    def adicionar_tipo_atendimento(self, identificador_tipo: int):
        if identificador_tipo not in self.__tipos_atendimento:
            self.__tipos_atendimento.append(identificador_tipo)

    def remover_tipo_atendimento(self, identificador_tipo: int):
        if identificador_tipo in self.__tipos_atendimento:
            self.__tipos_atendimento.remove(identificador_tipo)

    @property
    def profissionais(self):
        return self.__profissionais.copy()

    def adicionar_profissional(self, identificador_profissional: int):
        if identificador_profissional not in self.__profissionais:
            self.__profissionais.append(identificador_profissional)

    def remover_profissional(self, identificador_profissional: int):
        if identificador_profissional in self.__profissionais:
            self.__profissionais.remove(identificador_profissional)

    @property
    def pacientes(self):
        return self.__pacientes.copy()

    def adicionar_paciente(self, identificador_paciente: int):
        if identificador_paciente not in self.__pacientes:
            self.__pacientes.append(identificador_paciente)

    @property
    def atendimentos(self):
        return self.__atendimentos.copy()

    def adicionar_atendimento(self, identificador_atendimento: int):
        self.__atendimentos.append(identificador_atendimento)

    def __str__(self):
        return (f"ID: {self.identificador} | Nome: {self.nome} | Local: {self.localizacao} | "
                f"Horário: {self.horario_abertura.strftime('%H:%M')} às {self.horario_fechamento.strftime('%H:%M')} | "
                f"Contato: {self.contato}")