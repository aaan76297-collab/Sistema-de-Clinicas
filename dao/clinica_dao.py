class ClinicaDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__clinicas = {}

    def adicionar(self, clinica):
        self.__clinicas[clinica.identificador] = clinica

    def buscar_por_identificador(self, identificador):
        return self.__clinicas.get(identificador)

    def buscar_por_nome(self, nome):
        nome_lower = nome.lower()
        return [clinica for clinica in self.__clinicas.values() if nome_lower in clinica.nome.lower()]

    def listar_todos(self):
        return list(self.__clinicas.values())

    def atualizar(self, clinica):
        if clinica.identificador in self.__clinicas:
            self.__clinicas[clinica.identificador] = clinica

    def remover(self, identificador):
        if identificador in self.__clinicas:
            del self.__clinicas[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('clinica')