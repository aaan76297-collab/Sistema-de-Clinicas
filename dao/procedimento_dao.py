class ProcedimentoDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__procedimentos = {}

    def adicionar(self, procedimento):
        self.__procedimentos[procedimento.identificador] = procedimento

    def buscar_por_identificador(self, identificador):
        return self.__procedimentos.get(identificador)

    def buscar_por_descricao(self, descricao):
        descricao_lower = descricao.lower()
        return [procedimento for procedimento in self.__procedimentos.values() if descricao_lower in procedimento.descricao.lower()]

    def listar_todos(self):
        return list(self.__procedimentos.values())

    def atualizar(self, procedimento):
        if procedimento.identificador in self.__procedimentos:
            self.__procedimentos[procedimento.identificador] = procedimento

    def remover(self, identificador):
        if identificador in self.__procedimentos:
            del self.__procedimentos[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('procedimento')