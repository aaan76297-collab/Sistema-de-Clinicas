class PacienteDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__pacientes = {}

    def adicionar(self, paciente):
        self.__pacientes[paciente.identificador] = paciente

    def buscar_por_identificador(self, identificador):
        return self.__pacientes.get(identificador)

    def buscar_por_nome(self, nome):
        nome_lower = nome.lower()
        return [paciente for paciente in self.__pacientes.values() if nome_lower in paciente.nome.lower()]

    def buscar_por_cpf(self, cpf):
        for paciente in self.__pacientes.values():
            if paciente.cpf == cpf:
                return paciente
        return None

    def listar_todos(self):
        return list(self.__pacientes.values())

    def atualizar(self, paciente):
        if paciente.identificador in self.__pacientes:
            self.__pacientes[paciente.identificador] = paciente

    def remover(self, identificador):
        if identificador in self.__pacientes:
            del self.__pacientes[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('paciente')