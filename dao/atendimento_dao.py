class AtendimentoDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__atendimentos = {}

    def adicionar(self, atendimento):
        self.__atendimentos[atendimento.identificador] = atendimento

    def buscar_por_identificador(self, identificador):
        return self.__atendimentos.get(identificador)

    def listar_todos(self):
        return list(self.__atendimentos.values())

    def atualizar(self, atendimento):
        if atendimento.identificador in self.__atendimentos:
            self.__atendimentos[atendimento.identificador] = atendimento

    def remover(self, identificador):
        if identificador in self.__atendimentos:
            del self.__atendimentos[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('atendimento')