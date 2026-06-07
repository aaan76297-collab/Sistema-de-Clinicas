from model.procedimento import Procedimento
from dao.procedimento_dao import ProcedimentoDAO
from view.tela_procedimento import TelaProcedimento

class ProcedimentoController:
    def __init__(self, dao, tela):
        self.__dao = dao
        self.__tela = tela

    def adicionar(self):
        descricao, duracao, preco = self.__tela.formulario_adicionar()
        novo_id = self.__dao.proximo_identificador()
        procedimento = Procedimento(novo_id, descricao, duracao, preco)
        self.__dao.adicionar(procedimento)
        self.__tela.exibir_mensagem(f"Procedimento cadastrado com ID {novo_id}.")

    def pesquisar(self):
        tipo, valor = self.__tela.formulario_pesquisar()
        if tipo == 'id':
            proc = self.__dao.buscar_por_identificador(valor)
            self.__tela.mostrar_procedimento(proc)
        else:
            resultados = self.__dao.buscar_por_descricao(valor)
            self.__tela.mostrar_lista(resultados)

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        identificador = self.__tela.obter_inteiro("ID do procedimento a editar: ")
        procedimento = self.__dao.buscar_por_identificador(identificador)
        if not procedimento:
            self.__tela.exibir_mensagem("Procedimento não encontrado.")
            return
        procedimento_editado = self.__tela.formulario_editar(procedimento)
        if procedimento_editado:
            self.__dao.atualizar(procedimento_editado)
            self.__tela.exibir_mensagem("Procedimento atualizado.")

    def remover(self):
        identificador = self.__tela.obter_inteiro("ID do procedimento a remover: ")
        procedimento = self.__dao.buscar_por_identificador(identificador)
        if not procedimento:
            self.__tela.exibir_mensagem("Procedimento não encontrado.")
            return
        if self.__tela.confirmar_remocao(procedimento):
            self.__dao.remover(identificador)
            self.__tela.exibir_mensagem("Procedimento removido.")