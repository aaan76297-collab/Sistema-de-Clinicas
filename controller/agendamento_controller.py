from datetime import datetime, timedelta
from model.atendimento import Atendimento

class AgendamentoController:
    def __init__(self, paciente_dao, clinica_dao, profissional_dao, especialidade_dao,
                 tipo_atendimento_dao, atendimento_dao, gerador_id, tela):
        self.__paciente_dao = paciente_dao
        self.__clinica_dao = clinica_dao
        self.__profissional_dao = profissional_dao
        self.__especialidade_dao = especialidade_dao
        self.__tipo_atendimento_dao = tipo_atendimento_dao
        self.__atendimento_dao = atendimento_dao
        self.__gerador_id = gerador_id
        self.__tela = tela

    def realizar_agendamento(self):
        try:
            self.__tela.exibir_mensagem("===== NOVO AGENDAMENTO =====")

            pacientes = self.__paciente_dao.listar_todos()
            if not pacientes:
                self.__tela.exibir_mensagem("Nenhum paciente cadastrado.")
                return
            self.__tela.mostrar_lista_pacientes(pacientes)
            id_paciente = self.__tela.obter_inteiro("ID do paciente: ")
            paciente = self.__paciente_dao.buscar_por_identificador(id_paciente)
            if not paciente:
                self.__tela.exibir_mensagem("Paciente inválido.")
                return

            clinicas = self.__clinica_dao.listar_todos()
            if not clinicas:
                self.__tela.exibir_mensagem("Nenhuma clínica cadastrada.")
                return
            self.__tela.mostrar_lista_clinicas(clinicas)
            id_clinica = self.__tela.obter_inteiro("ID da clínica: ")
            clinica = self.__clinica_dao.buscar_por_identificador(id_clinica)
            if not clinica:
                self.__tela.exibir_mensagem("Clínica inválida.")
                return

            profissionais_clinica = []
            for pid in clinica.profissionais:
                prof = self.__profissional_dao.buscar_por_identificador(pid)
                if prof:
                    profissionais_clinica.append(prof)

            especialidades_disponiveis = []
            for prof in profissionais_clinica:
                esp = self.__especialidade_dao.buscar_por_identificador(prof.especialidade_identificador)
                if esp and esp not in especialidades_disponiveis:
                    especialidades_disponiveis.append(esp)

            if not especialidades_disponiveis:
                self.__tela.exibir_mensagem("Nenhuma especialidade disponível nesta clínica.")
                return
            self.__tela.mostrar_lista_especialidades(especialidades_disponiveis)
            id_especialidade = self.__tela.obter_inteiro("ID da especialidade desejada: ")
            especialidade = self.__especialidade_dao.buscar_por_identificador(id_especialidade)
            if not especialidade or especialidade not in especialidades_disponiveis:
                self.__tela.exibir_mensagem("Especialidade indisponível.")
                return

            profissionais_validos = [p for p in profissionais_clinica if p.especialidade_identificador == id_especialidade]
            if not profissionais_validos:
                self.__tela.exibir_mensagem("Nenhum profissional com essa especialidade disponível.")
                return
            self.__tela.mostrar_lista_profissionais(profissionais_validos)
            id_profissional = self.__tela.obter_inteiro("ID do profissional: ")
            profissional = self.__profissional_dao.buscar_por_identificador(id_profissional)
            if not profissional or profissional not in profissionais_validos:
                self.__tela.exibir_mensagem("Profissional inválido.")
                return

            data_agendamento = self.__tela.obter_data("Data do atendimento")

            try:
                idade_paciente = paciente.idade(data_agendamento)
                if idade_paciente < 18:
                    self.__tela.exibir_mensagem("Erro: Paciente menor de 18 anos. Atendimento independente não permitido.")
                    return
            except ValueError as erro:
                self.__tela.exibir_mensagem(f"Erro na data de nascimento: {erro}")
                return

            dia_semana = data_agendamento.weekday()
            if dia_semana not in clinica.dias_funcionamento:
                self.__tela.exibir_mensagem("Erro: Clínica não funciona neste dia da semana.")
                return
            if dia_semana not in profissional.dias_trabalho:
                self.__tela.exibir_mensagem("Erro: Profissional não trabalha neste dia.")
                return

            horario_inicio = self.__tela.obter_hora("Horário de início")

            if not clinica.tipos_atendimento:
                self.__tela.exibir_mensagem("Erro: Clínica não possui tipos de atendimento cadastrados.")
                return
            tipos_clinica = []
            for tid in clinica.tipos_atendimento:
                tipo = self.__tipo_atendimento_dao.buscar_por_identificador(tid)
                if tipo:
                    tipos_clinica.append(tipo)
            self.__tela.mostrar_lista_tipos_atendimento(tipos_clinica)
            id_tipo = self.__tela.obter_inteiro("ID do tipo de atendimento: ")
            tipo_atend = self.__tipo_atendimento_dao.buscar_por_identificador(id_tipo)
            if not tipo_atend or tipo_atend not in tipos_clinica:
                self.__tela.exibir_mensagem("Erro: Tipo de atendimento inválido ou não disponível na clínica.")
                return

            duracao = tipo_atend.duracao_maxima
            horario_fim = (datetime.combine(data_agendamento, horario_inicio) + timedelta(minutes=duracao)).time()

            if horario_inicio < clinica.horario_abertura or horario_fim > clinica.horario_fechamento:
                self.__tela.exibir_mensagem("Erro: Atendimento fora do horário de funcionamento da clínica.")
                return

            if horario_inicio < profissional.horario_inicio or horario_fim > profissional.horario_fim:
                self.__tela.exibir_mensagem("Erro: Horário fora do expediente do profissional.")
                return

            for atend_existente in self.__atendimento_dao.listar_todos():
                if atend_existente.profissional_identificador == profissional.identificador and atend_existente.data == data_agendamento:
                    if not (horario_fim <= atend_existente.horario_inicio or horario_inicio >= atend_existente.horario_fim):
                        self.__tela.exibir_mensagem("Erro: Conflito de horário com outro atendimento do profissional.")
                        return

            novo_id = self.__gerador_id.proximo_id('atendimento')
            atendimento = Atendimento(
                novo_id, clinica.identificador, paciente.identificador,
                profissional.identificador, tipo_atend.identificador,
                especialidade.identificador, data_agendamento,
                horario_inicio, horario_fim, 0.0, "agendado"
            )
            self.__atendimento_dao.adicionar(atendimento)
            clinica.adicionar_atendimento(novo_id)
            paciente.adicionar_atendimento(novo_id)
            profissional.adicionar_atendimento(novo_id)
            self.__tela.exibir_mensagem(f"Agendamento criado com ID {novo_id} (status: agendado).")

        except Exception as erro:
            self.__tela.exibir_mensagem(f"Erro inesperado no agendamento: {erro}")