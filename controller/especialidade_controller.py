from model.especialidade import Especialidade
from dao.especialidade_dao import EspecialidadeDAO
from view.tela_especialidade import TelaEspecialidade

class EspecialidadeController:
    def __init__(self, dao, tela):
        self.__dao = dao
        self.__tela = tela

    def adicionar(self):
        nome, descricao = self.__tela.formulario_adicionar()
        novo_id = self.__dao.proximo_identificador()
        especialidade = Especialidade(novo_id, nome, descricao)
        self.__dao.adicionar(especialidade)
        self.__tela.exibir_mensagem(f"Especialidade cadastrada com ID {novo_id}.")

    def pesquisar(self):
        tipo, valor = self.__tela.formulario_pesquisar()
        if tipo == 'id':
            especialidade = self.__dao.buscar_por_identificador(valor)
            self.__tela.mostrar_especialidade(especialidade)
        else:
            resultados = self.__dao.buscar_por_nome(valor)
            self.__tela.mostrar_lista(resultados)

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        identificador = self.__tela.obter_inteiro("ID da especialidade a editar: ")
        especialidade = self.__dao.buscar_por_identificador(identificador)
        if not especialidade:
            self.__tela.exibir_mensagem("Especialidade não encontrada.")
            return
        especialidade_editada = self.__tela.formulario_editar(especialidade)
        if especialidade_editada:
            self.__dao.atualizar(especialidade_editada)
            self.__tela.exibir_mensagem("Especialidade atualizada.")

    def remover(self):
        identificador = self.__tela.obter_inteiro("ID da especialidade a remover: ")
        especialidade = self.__dao.buscar_por_identificador(identificador)
        if not especialidade:
            self.__tela.exibir_mensagem("Especialidade não encontrada.")
            return
        if self.__tela.confirmar_remocao(especialidade):
            self.__dao.remover(identificador)
            self.__tela.exibir_mensagem("Especialidade removida.")