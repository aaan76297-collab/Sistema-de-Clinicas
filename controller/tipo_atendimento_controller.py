from model.tipo_atendimento import TipoAtendimento
from dao.tipo_atendimento_dao import TipoAtendimentoDAO
from view.tela_tipo_atendimento import TelaTipoAtendimento

class TipoAtendimentoController:
    def __init__(self, dao, tela):
        self.__dao = dao
        self.__tela = tela

    def adicionar(self):
        nome, descricao, duracao = self.__tela.formulario_adicionar()
        novo_id = self.__dao.proximo_identificador()
        tipo = TipoAtendimento(novo_id, nome, descricao, duracao)
        self.__dao.adicionar(tipo)
        self.__tela.exibir_mensagem(f"Tipo de atendimento cadastrado com ID {novo_id}.")

    def pesquisar(self):
        tipo, valor = self.__tela.formulario_pesquisar()
        if tipo == 'id':
            tipo_atend = self.__dao.buscar_por_identificador(valor)
            self.__tela.mostrar_tipo(tipo_atend)
        else:
            resultados = self.__dao.buscar_por_nome(valor)
            self.__tela.mostrar_lista(resultados)

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        identificador = self.__tela.obter_inteiro("ID do tipo a editar: ")
        tipo = self.__dao.buscar_por_identificador(identificador)
        if not tipo:
            self.__tela.exibir_mensagem("Tipo de atendimento não encontrado.")
            return
        tipo_editado = self.__tela.formulario_editar(tipo)
        if tipo_editado:
            self.__dao.atualizar(tipo_editado)
            self.__tela.exibir_mensagem("Tipo de atendimento atualizado.")

    def remover(self):
        identificador = self.__tela.obter_inteiro("ID do tipo a remover: ")
        tipo = self.__dao.buscar_por_identificador(identificador)
        if not tipo:
            self.__tela.exibir_mensagem("Tipo de atendimento não encontrado.")
            return
        if self.__tela.confirmar_remocao(tipo):
            self.__dao.remover(identificador)
            self.__tela.exibir_mensagem("Tipo de atendimento removido.")