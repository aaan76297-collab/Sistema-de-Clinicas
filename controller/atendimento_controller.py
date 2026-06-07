from model.atendimento import Atendimento

class AtendimentoController:
    def __init__(self, dao, tela):
        self.__dao = dao
        self.__tela = tela

    def adicionar(self):
        self.__tela.exibir_mensagem("Use a opção de Agendamento para criar um atendimento.")

    def pesquisar(self):
        try:
            identificador = self.__tela.obter_inteiro("ID do atendimento: ")
            atendimento = self.__dao.buscar_por_identificador(identificador)
            self.__tela.mostrar_atendimento(atendimento)
        except Exception as erro:
            self.__tela.exibir_mensagem(f"Erro na pesquisa: {erro}")

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        try:
            identificador = self.__tela.obter_inteiro("ID do atendimento a editar: ")
            atendimento = self.__dao.buscar_por_identificador(identificador)
            if not atendimento:
                self.__tela.exibir_mensagem("Atendimento não encontrado.")
                return

            self.__tela.mostrar_atendimento(atendimento)
            if not self.__tela.confirmar("Deseja editar este atendimento?"):
                return

            novo_status = self.__tela.obter_texto(f"Novo status [{atendimento.status}]: ", obrigatorio=False)
            if novo_status:
                if novo_status not in Atendimento.STATUS_VALIDOS:
                    self.__tela.exibir_mensagem("Status inválido.")
                    return

                atendimento.status = novo_status

            self.__dao.atualizar(atendimento)
            self.__tela.exibir_mensagem("Atendimento atualizado.")
        except Exception as erro:
            self.__tela.exibir_mensagem(f"Erro ao editar atendimento: {erro}")

    def remover(self):
        try:
            identificador = self.__tela.obter_inteiro("ID do atendimento a remover: ")
            atendimento = self.__dao.buscar_por_identificador(identificador)
            if not atendimento:
                self.__tela.exibir_mensagem("Atendimento não encontrado.")
                return
            if self.__tela.confirmar_remocao(atendimento):
                self.__dao.remover(identificador)
                self.__tela.exibir_mensagem("Atendimento removido.")
        except Exception as erro:
            self.__tela.exibir_mensagem(f"Erro ao remover atendimento: {erro}")