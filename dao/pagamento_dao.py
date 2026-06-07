class PagamentoDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__pagamentos = {}

    def adicionar(self, pagamento):
        self.__pagamentos[pagamento.identificador] = pagamento

    def buscar_por_identificador(self, identificador):
        return self.__pagamentos.get(identificador)

    def listar_todos(self):
        return list(self.__pagamentos.values())

    def atualizar(self, pagamento):
        if pagamento.identificador in self.__pagamentos:
            self.__pagamentos[pagamento.identificador] = pagamento

    def remover(self, identificador):
        if identificador in self.__pagamentos:
            del self.__pagamentos[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('pagamento')