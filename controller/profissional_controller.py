from model.profissional import Profissional
from model.contato import Contato
from model.especialidade import Especialidade
from dao.profissional_dao import ProfissionalDAO
from dao.especialidade_dao import EspecialidadeDAO
from view.tela_profissional import TelaProfissional

class ProfissionalController:
    def __init__(self, dao, especialidade_dao, tela):
        self.__dao = dao
        self.__especialidade_dao = especialidade_dao
        self.__tela = tela

    def adicionar(self):
        nome, cpf, registro, dias_trabalho, horario_inicio, horario_fim, telefone, email, especialidade_id = self.__tela.formulario_adicionar()
        if self.__dao.buscar_por_registro(registro):
            self.__tela.exibir_mensagem("Já existe profissional com este registro.")
            return
        if especialidade_id == 0:
            especialidade_id = self.__tela.cadastrar_nova_especialidade(self.__especialidade_dao)
            if not especialidade_id:
                return
        elif not self.__especialidade_dao.buscar_por_identificador(especialidade_id):
            self.__tela.exibir_mensagem("Especialidade inválida.")
            return

        contato = Contato(telefone, email)
        novo_id = self.__dao.proximo_identificador()
        profissional = Profissional(novo_id, nome, contato, cpf, registro, especialidade_id,
                                    dias_trabalho, horario_inicio, horario_fim)
        self.__dao.adicionar(profissional)
        self.__tela.exibir_mensagem(f"Profissional cadastrado com ID {novo_id}.")

    def pesquisar(self):
        tipo, valor = self.__tela.formulario_pesquisar()
        if tipo == 'id':
            profissional = self.__dao.buscar_por_identificador(valor)
            self.__tela.mostrar_profissional(profissional)
        elif tipo == 'nome':
            resultados = self.__dao.buscar_por_nome(valor)
            self.__tela.mostrar_lista(resultados)
        elif tipo == 'registro':
            profissional = self.__dao.buscar_por_registro(valor)
            self.__tela.mostrar_profissional(profissional)

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        identificador = self.__tela.obter_inteiro("ID do profissional a editar: ")
        profissional = self.__dao.buscar_por_identificador(identificador)
        if not profissional:
            self.__tela.exibir_mensagem("Profissional não encontrado.")
            return
        profissional_editado = self.__tela.formulario_editar(profissional)
        if profissional_editado:
            self.__dao.atualizar(profissional_editado)
            self.__tela.exibir_mensagem("Profissional atualizado.")

    def remover(self):
        identificador = self.__tela.obter_inteiro("ID do profissional a remover: ")
        profissional = self.__dao.buscar_por_identificador(identificador)
        if not profissional:
            self.__tela.exibir_mensagem("Profissional não encontrado.")
            return
        if self.__tela.confirmar_remocao(profissional):
            self.__dao.remover(identificador)
            self.__tela.exibir_mensagem("Profissional removido.")