class GeradorID:
    def __init__(self):
        self.__contadores = {
            'clinica': 1,
            'paciente': 1,
            'profissional': 1,
            'tipo_atendimento': 1,
            'especialidade': 1,
            'procedimento': 1,
            'atendimento': 1,
            'pagamento': 1
        }

    def proximo_id(self, tipo):
        atual = self.__contadores[tipo]
        self.__contadores[tipo] += 1
        return atual