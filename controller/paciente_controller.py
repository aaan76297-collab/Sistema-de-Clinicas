from model.paciente import Paciente
from model.contato import Contato
from dao.paciente_dao import PacienteDAO
from view.tela_paciente import TelaPaciente

class PacienteController:
    def __init__(self, dao, tela):
        self.__dao = dao
        self.__tela = tela

    def adicionar(self):
        nome, cpf, data_nasc, telefone, email = self.__tela.formulario_adicionar()
        if self.__dao.buscar_por_cpf(cpf):
            self.__tela.exibir_mensagem("Já existe paciente com este CPF.")
            return
        contato = Contato(telefone, email)
        novo_id = self.__dao.proximo_identificador()
        paciente = Paciente(novo_id, nome, contato, cpf, data_nasc)
        self.__dao.adicionar(paciente)
        self.__tela.exibir_mensagem(f"Paciente cadastrado com ID {novo_id}.")

    def pesquisar(self):
        tipo, valor = self.__tela.formulario_pesquisar()
        if tipo == 'id':
            paciente = self.__dao.buscar_por_identificador(valor)
            self.__tela.mostrar_paciente(paciente)
        elif tipo == 'nome':
            resultados = self.__dao.buscar_por_nome(valor)
            self.__tela.mostrar_lista(resultados)
        elif tipo == 'cpf':
            paciente = self.__dao.buscar_por_cpf(valor)
            self.__tela.mostrar_paciente(paciente)

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        identificador = self.__tela.obter_inteiro("ID do paciente a editar: ")
        paciente = self.__dao.buscar_por_identificador(identificador)
        if not paciente:
            self.__tela.exibir_mensagem("Paciente não encontrado.")
            return
        paciente_editado = self.__tela.formulario_editar(paciente)
        if paciente_editado:
            self.__dao.atualizar(paciente_editado)
            self.__tela.exibir_mensagem("Paciente atualizado.")

    def remover(self):
        identificador = self.__tela.obter_inteiro("ID do paciente a remover: ")
        paciente = self.__dao.buscar_por_identificador(identificador)
        if not paciente:
            self.__tela.exibir_mensagem("Paciente não encontrado.")
            return
        if self.__tela.confirmar_remocao(paciente):
            self.__dao.remover(identificador)
            self.__tela.exibir_mensagem("Paciente removido.")