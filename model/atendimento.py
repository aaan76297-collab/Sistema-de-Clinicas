from datetime import date, time

class Atendimento:
    STATUS_VALIDOS = ["agendado", "confirmado", "atendimento realizado", "cancelado"]

    def __init__(self, identificador: int, clinica_identificador: int, paciente_identificador: int,
                 profissional_identificador: int, tipo_atendimento_identificador: int,
                 especialidade_identificador: int, data_atendimento: date,
                 horario_inicio: time, horario_fim: time, valor_total: float,
                 status: str = "agendado"):
        self.__identificador = identificador
        self.__clinica_identificador = clinica_identificador
        self.__paciente_identificador = paciente_identificador
        self.__profissional_identificador = profissional_identificador
        self.__tipo_atendimento_identificador = tipo_atendimento_identificador
        self.__especialidade_identificador = especialidade_identificador
        self.__data = data_atendimento
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor_total = valor_total
        self.__status = status
        self.__procedimentos_realizados = []
        self.__pagamentos = []

    @property
    def identificador(self):
        return self.__identificador

    @property
    def clinica_identificador(self):
        return self.__clinica_identificador

    @property
    def paciente_identificador(self):
        return self.__paciente_identificador

    @property
    def profissional_identificador(self):
        return self.__profissional_identificador

    @property
    def tipo_atendimento_identificador(self):
        return self.__tipo_atendimento_identificador

    @property
    def especialidade_identificador(self):
        return self.__especialidade_identificador

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        self.__data = valor

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor):
        self.__valor_total = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        if valor in self.STATUS_VALIDOS:
            self.__status = valor
        else:
            raise ValueError(f"Status inválido: {valor}")

    @property
    def procedimentos_realizados(self):
        return self.__procedimentos_realizados.copy()

    def adicionar_procedimento(self, procedimento_realizado):
        self.__procedimentos_realizados.append(procedimento_realizado)

    @property
    def pagamentos(self):
        return self.__pagamentos.copy()

    def adicionar_pagamento(self, pagamento):
        self.__pagamentos.append(pagamento)

    def remover_pagamento(self, pagamento):
        if pagamento in self.__pagamentos:
            self.__pagamentos.remove(pagamento)

    def __str__(self):
        return (f"ID: {self.identificador} | Data: {self.data.strftime('%d/%m/%Y')} | "
                f"{self.horario_inicio.strftime('%H:%M')} - {self.horario_fim.strftime('%H:%M')} | "
                f"Status: {self.status} | Valor: R$ {self.valor_total:.2f}")
