class ProfissionalDAO:
    def __init__(self, gerador_id):
        self.__gerador_id = gerador_id
        self.__profissionais = {}

    def adicionar(self, profissional):
        self.__profissionais[profissional.identificador] = profissional

    def buscar_por_identificador(self, identificador):
        return self.__profissionais.get(identificador)

    def buscar_por_nome(self, nome):
        nome_lower = nome.lower()
        return [profissional for profissional in self.__profissionais.values() if nome_lower in profissional.nome.lower()]

    def buscar_por_registro(self, registro):
        for profissional in self.__profissionais.values():
            if profissional.registro_profissional == registro:
                return profissional
        return None

    def listar_todos(self):
        return list(self.__profissionais.values())

    def atualizar(self, profissional):
        if profissional.identificador in self.__profissionais:
            self.__profissionais[profissional.identificador] = profissional

    def remover(self, identificador):
        if identificador in self.__profissionais:
            del self.__profissionais[identificador]
            return True
        return False

    def proximo_identificador(self):
        return self.__gerador_id.proximo_id('profissional')