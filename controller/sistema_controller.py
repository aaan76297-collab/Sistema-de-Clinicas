from dao.gerador_id import GeradorID
from dao.clinica_dao import ClinicaDAO
from dao.paciente_dao import PacienteDAO
from dao.profissional_dao import ProfissionalDAO
from dao.tipo_atendimento_dao import TipoAtendimentoDAO
from dao.especialidade_dao import EspecialidadeDAO
from dao.procedimento_dao import ProcedimentoDAO
from dao.atendimento_dao import AtendimentoDAO
from dao.pagamento_dao import PagamentoDAO

from view.tela_principal import TelaPrincipal
from view.tela_clinica import TelaClinica
from view.tela_paciente import TelaPaciente
from view.tela_profissional import TelaProfissional
from view.tela_tipo_atendimento import TelaTipoAtendimento
from view.tela_especialidade import TelaEspecialidade
from view.tela_procedimento import TelaProcedimento
from view.tela_atendimento import TelaAtendimento
from view.tela_pagamento import TelaPagamento
from view.tela_agendamento import TelaAgendamento
from view.tela_relatorio import TelaRelatorio

from controller.clinica_controller import ClinicaController
from controller.paciente_controller import PacienteController
from controller.profissional_controller import ProfissionalController
from controller.tipo_atendimento_controller import TipoAtendimentoController
from controller.especialidade_controller import EspecialidadeController
from controller.procedimento_controller import ProcedimentoController
from controller.atendimento_controller import AtendimentoController
from controller.pagamento_controller import PagamentoController
from controller.agendamento_controller import AgendamentoController
from controller.relatorio_controller import RelatorioController

class SistemaController:
    def __init__(self):
        self.__gerador_id = GeradorID()

        # DAOs
        self.__dao_clinica = ClinicaDAO(self.__gerador_id)
        self.__dao_paciente = PacienteDAO(self.__gerador_id)
        self.__dao_profissional = ProfissionalDAO(self.__gerador_id)
        self.__dao_tipo_atendimento = TipoAtendimentoDAO(self.__gerador_id)
        self.__dao_especialidade = EspecialidadeDAO(self.__gerador_id)
        self.__dao_procedimento = ProcedimentoDAO(self.__gerador_id)
        self.__dao_atendimento = AtendimentoDAO(self.__gerador_id)
        self.__dao_pagamento = PagamentoDAO(self.__gerador_id)

        # Telas
        self.__tela_principal = TelaPrincipal()
        self.__tela_clinica = TelaClinica()
        self.__tela_paciente = TelaPaciente()
        self.__tela_profissional = TelaProfissional()
        self.__tela_tipo_atendimento = TelaTipoAtendimento()
        self.__tela_especialidade = TelaEspecialidade()
        self.__tela_procedimento = TelaProcedimento()
        self.__tela_atendimento = TelaAtendimento()
        self.__tela_pagamento = TelaPagamento()
        self.__tela_agendamento = TelaAgendamento()
        self.__tela_relatorio = TelaRelatorio()

        # Controllers
        self.__clinica_controller = ClinicaController(
            self.__dao_clinica,
            self.__dao_profissional,
            self.__dao_tipo_atendimento,
            self.__tela_clinica
        )
        self.__paciente_controller = PacienteController(self.__dao_paciente, self.__tela_paciente)
        self.__profissional_controller = ProfissionalController(
            self.__dao_profissional, self.__dao_especialidade, self.__tela_profissional
        )
        self.__tipo_atendimento_controller = TipoAtendimentoController(
            self.__dao_tipo_atendimento, self.__tela_tipo_atendimento
        )
        self.__especialidade_controller = EspecialidadeController(
            self.__dao_especialidade, self.__tela_especialidade
        )
        self.__procedimento_controller = ProcedimentoController(
            self.__dao_procedimento, self.__tela_procedimento
        )
        self.__atendimento_controller = AtendimentoController(
            self.__dao_atendimento, self.__tela_atendimento
        )
        self.__pagamento_controller = PagamentoController(
            self.__dao_pagamento, self.__dao_atendimento, self.__tela_pagamento
        )
        self.__agendamento_controller = AgendamentoController(
            self.__dao_paciente,
            self.__dao_clinica,
            self.__dao_profissional,
            self.__dao_especialidade,
            self.__dao_tipo_atendimento,
            self.__dao_atendimento,
            self.__gerador_id,
            self.__tela_agendamento
        )
        self.__relatorio_controller = RelatorioController(
            self.__dao_clinica, self.__dao_atendimento, self.__dao_procedimento, self.__tela_relatorio
        )

    def executar(self):
        while True:
            try:
                opcao = self.__tela_principal.menu_principal()
                if opcao == '0':
                    if self.__tela_principal.confirmar("Deseja encerrar o sistema?"):
                        self.__tela_principal.exibir_mensagem("Encerrando...")
                        break
                elif opcao == '1':
                    self.__agendamento_controller.realizar_agendamento()
                elif opcao == '2':
                    self.menu_cadastros()
                elif opcao == '3':
                    self.menu_navegar()
                elif opcao == '4':
                    self.menu_gerenciar()
                elif opcao == '5':
                    self.menu_relatorios()
                else:
                    self.__tela_principal.exibir_mensagem("Opção inválida.")
            except Exception as erro:
                self.__tela_principal.exibir_mensagem(f"Erro inesperado: {erro}")
            finally:
                self.__tela_principal.pausa()

    def menu_cadastros(self):
        while True:
            op = self.__tela_principal.menu_cadastros()
            if op == '0':
                break
            elif op == '1':
                self.__clinica_controller.adicionar()
            elif op == '2':
                self.__paciente_controller.adicionar()
            elif op == '3':
                self.__profissional_controller.adicionar()
            elif op == '4':
                self.__tipo_atendimento_controller.adicionar()
            elif op == '5':
                self.__especialidade_controller.adicionar()
            elif op == '6':
                self.__procedimento_controller.adicionar()
            self.__tela_principal.pausa()

    def menu_navegar(self):
        while True:
            op = self.__tela_principal.menu_navegar()
            if op == '0':
                break
            print("\n1. Listar todos")
            print("2. Pesquisar")
            print("0. Voltar")
            sub_op = self.__tela_principal.obter_opcao("Opção: ", ['0','1','2'])
            if sub_op == '0':
                continue
            if op == '1':
                if sub_op == '1': self.__clinica_controller.ver_todos()
                else: self.__clinica_controller.pesquisar()
            elif op == '2':
                if sub_op == '1': self.__paciente_controller.ver_todos()
                else: self.__paciente_controller.pesquisar()
            elif op == '3':
                if sub_op == '1': self.__profissional_controller.ver_todos()
                else: self.__profissional_controller.pesquisar()
            elif op == '4':
                if sub_op == '1': self.__tipo_atendimento_controller.ver_todos()
                else: self.__tipo_atendimento_controller.pesquisar()
            elif op == '5':
                if sub_op == '1': self.__especialidade_controller.ver_todos()
                else: self.__especialidade_controller.pesquisar()
            elif op == '6':
                if sub_op == '1': self.__procedimento_controller.ver_todos()
                else: self.__procedimento_controller.pesquisar()
            elif op == '7':
                if sub_op == '1': self.__atendimento_controller.ver_todos()
                else: self.__atendimento_controller.pesquisar()
            elif op == '8':
                if sub_op == '1': self.__pagamento_controller.ver_todos()
                else: self.__pagamento_controller.pesquisar()
            self.__tela_principal.pausa()

    def menu_gerenciar(self):
        while True:
            op = self.__tela_principal.menu_gerenciar()
            if op == '0':
                break
            while True:
                if op == '1': opcao_crud = self.__tela_clinica.menu_crud()
                elif op == '2': opcao_crud = self.__tela_paciente.menu_crud()
                elif op == '3': opcao_crud = self.__tela_profissional.menu_crud()
                elif op == '4': opcao_crud = self.__tela_tipo_atendimento.menu_crud()
                elif op == '5': opcao_crud = self.__tela_especialidade.menu_crud()
                elif op == '6': opcao_crud = self.__tela_procedimento.menu_crud()
                elif op == '7': opcao_crud = self.__tela_atendimento.menu_crud()
                elif op == '8': opcao_crud = self.__tela_pagamento.menu_crud()
                else: break
                if opcao_crud == '0': break
                if op == '1': self.executar_crud_clinica(opcao_crud)
                elif op == '2': self.executar_crud_paciente(opcao_crud)
                elif op == '3': self.executar_crud_profissional(opcao_crud)
                elif op == '4': self.executar_crud_tipo_atendimento(opcao_crud)
                elif op == '5': self.executar_crud_especialidade(opcao_crud)
                elif op == '6': self.executar_crud_procedimento(opcao_crud)
                elif op == '7': self.executar_crud_atendimento(opcao_crud)
                elif op == '8': self.executar_crud_pagamento(opcao_crud)
                self.__tela_principal.pausa()

    def executar_crud_clinica(self, opcao):
        if opcao == '1': self.__clinica_controller.adicionar()
        elif opcao == '2': self.__clinica_controller.pesquisar()
        elif opcao == '3': self.__clinica_controller.ver_todos()
        elif opcao == '4': self.__clinica_controller.editar()
        elif opcao == '5': self.__clinica_controller.remover()
        elif opcao == '6': self.__clinica_controller.vincular_profissional()
        elif opcao == '7': self.__clinica_controller.desvincular_profissional()
        elif opcao == '8': self.__clinica_controller.vincular_tipo_atendimento()
        elif opcao == '9': self.__clinica_controller.desvincular_tipo_atendimento()

    def executar_crud_paciente(self, opcao):
        if opcao == '1': self.__paciente_controller.adicionar()
        elif opcao == '2': self.__paciente_controller.pesquisar()
        elif opcao == '3': self.__paciente_controller.ver_todos()
        elif opcao == '4': self.__paciente_controller.editar()
        elif opcao == '5': self.__paciente_controller.remover()

    def executar_crud_profissional(self, opcao):
        if opcao == '1': self.__profissional_controller.adicionar()
        elif opcao == '2': self.__profissional_controller.pesquisar()
        elif opcao == '3': self.__profissional_controller.ver_todos()
        elif opcao == '4': self.__profissional_controller.editar()
        elif opcao == '5': self.__profissional_controller.remover()

    def executar_crud_tipo_atendimento(self, opcao):
        if opcao == '1': self.__tipo_atendimento_controller.adicionar()
        elif opcao == '2': self.__tipo_atendimento_controller.pesquisar()
        elif opcao == '3': self.__tipo_atendimento_controller.ver_todos()
        elif opcao == '4': self.__tipo_atendimento_controller.editar()
        elif opcao == '5': self.__tipo_atendimento_controller.remover()

    def executar_crud_especialidade(self, opcao):
        if opcao == '1': self.__especialidade_controller.adicionar()
        elif opcao == '2': self.__especialidade_controller.pesquisar()
        elif opcao == '3': self.__especialidade_controller.ver_todos()
        elif opcao == '4': self.__especialidade_controller.editar()
        elif opcao == '5': self.__especialidade_controller.remover()

    def executar_crud_procedimento(self, opcao):
        if opcao == '1': self.__procedimento_controller.adicionar()
        elif opcao == '2': self.__procedimento_controller.pesquisar()
        elif opcao == '3': self.__procedimento_controller.ver_todos()
        elif opcao == '4': self.__procedimento_controller.editar()
        elif opcao == '5': self.__procedimento_controller.remover()

    def executar_crud_atendimento(self, opcao):
        if opcao == '1': self.__atendimento_controller.adicionar()
        elif opcao == '2': self.__atendimento_controller.pesquisar()
        elif opcao == '3': self.__atendimento_controller.ver_todos()
        elif opcao == '4': self.__atendimento_controller.editar()
        elif opcao == '5': self.__atendimento_controller.remover()

    def executar_crud_pagamento(self, opcao):
        if opcao == '1': self.__pagamento_controller.adicionar()
        elif opcao == '2': self.__pagamento_controller.pesquisar()
        elif opcao == '3': self.__pagamento_controller.ver_todos()
        elif opcao == '4': self.__pagamento_controller.editar()
        elif opcao == '5': self.__pagamento_controller.remover()

    def menu_relatorios(self):
        while True:
            op = self.__tela_principal.menu_relatorios()
            if op == '0':
                break
            if op == '1':
                self.__relatorio_controller.ranking_clinicas_atendimentos()
            elif op == '2':
                self.__relatorio_controller.atendimentos_mais_caro_barato()
            elif op == '3':
                self.__relatorio_controller.procedimentos_mais_realizados()
            elif op == '4':
                self.__relatorio_controller.procedimentos_mais_caro_barato_catalogo()
            self.__tela_principal.pausa()


if __name__ == "__main__":
    sistema = SistemaController()
    sistema.executar()