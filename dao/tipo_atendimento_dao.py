class TipoAtendimentoDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__tipos_atendimento = {}

    def adicionar(self, tipo_atendimento):
        self.__tipos_atendimento[tipo_atendimento.identificador] = tipo_atendimento

    def buscar_por_identificador(self, identificador):
        return self.__tipos_atendimento.get(identificador)

    def buscar_por_nome(self, nome):
        nome_lower = nome.lower()
        return [tipo for tipo in self.__tipos_atendimento.values() if nome_lower in tipo.nome.lower()]

    def listar_todos(self):
        return list(self.__tipos_atendimento.values())

    def atualizar(self, tipo_atendimento):
        if tipo_atendimento.identificador in self.__tipos_atendimento:
            self.__tipos_atendimento[tipo_atendimento.identificador] = tipo_atendimento

    def remover(self, identificador):
        if identificador in self.__tipos_atendimento:
            del self.__tipos_atendimento[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('tipo_atendimento')