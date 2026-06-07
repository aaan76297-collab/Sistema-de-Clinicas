class EspecialidadeDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__especialidades = {}

    def adicionar(self, especialidade):
        self.__especialidades[especialidade.identificador] = especialidade

    def buscar_por_identificador(self, identificador):
        return self.__especialidades.get(identificador)

    def buscar_por_nome(self, nome):
        nome_lower = nome.lower()
        return [especialidade for especialidade in self.__especialidades.values() if nome_lower in especialidade.nome.lower()]

    def listar_todos(self):
        return list(self.__especialidades.values())

    def atualizar(self, especialidade):
        if especialidade.identificador in self.__especialidades:
            self.__especialidades[especialidade.identificador] = especialidade

    def remover(self, identificador):
        if identificador in self.__especialidades:
            del self.__especialidades[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('especialidade')