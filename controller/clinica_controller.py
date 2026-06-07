from model.clinica import Clinica
from model.contato import Contato

class ClinicaController:
    def __init__(self, dao_clinica, dao_profissional, dao_tipo_atendimento, tela):
        self.__dao = dao_clinica
        self.__dao_profissional = dao_profissional
        self.__dao_tipo_atendimento = dao_tipo_atendimento
        self.__tela = tela

    def adicionar(self):
        nome, localizacao, descricao, abertura, fechamento, dias, telefone, email = self.__tela.formulario_adicionar()
        contato = Contato(telefone, email)
        novo_id = self.__dao.proximo_identificador()
        clinica = Clinica(novo_id, nome, localizacao, descricao, abertura, fechamento, dias, contato)
        self.__dao.adicionar(clinica)
        self.__tela.exibir_mensagem(f"Clínica cadastrada com ID {novo_id}.")

    def pesquisar(self):
        tipo, valor = self.__tela.formulario_pesquisar()
        if tipo == 'id':
            clinica = self.__dao.buscar_por_identificador(valor)
            self.__tela.mostrar_clinica(clinica)
        else:
            resultados = self.__dao.buscar_por_nome(valor)
            self.__tela.mostrar_lista(resultados)

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        identificador = self.__tela.obter_inteiro("ID da clínica a editar: ")
        clinica = self.__dao.buscar_por_identificador(identificador)
        if not clinica:
            self.__tela.exibir_mensagem("Clínica não encontrada.")
            return
        clinica_editada = self.__tela.formulario_editar(clinica)
        if clinica_editada:
            self.__dao.atualizar(clinica_editada)
            self.__tela.exibir_mensagem("Clínica atualizada.")

    def remover(self):
        identificador = self.__tela.obter_inteiro("ID da clínica a remover: ")
        clinica = self.__dao.buscar_por_identificador(identificador)
        if not clinica:
            self.__tela.exibir_mensagem("Clínica não encontrada.")
            return
        if self.__tela.confirmar_remocao(clinica):
            self.__dao.remover(identificador)
            self.__tela.exibir_mensagem("Clínica removida.")

    def vincular_profissional(self):
        id_clinica = self.__tela.obter_inteiro("ID da clínica: ")
        clinica = self.__dao.buscar_por_identificador(id_clinica)
        if not clinica:
            self.__tela.exibir_mensagem("Clínica não encontrada.")
            return
        id_prof = self.__tela.obter_id_profissional()
        profissional = self.__dao_profissional.buscar_por_identificador(id_prof)
        if not profissional:
            self.__tela.exibir_mensagem("Profissional não encontrado.")
            return
        clinica.adicionar_profissional(profissional.identificador)
        profissional.adicionar_clinica(clinica.identificador)
        self.__tela.exibir_mensagem("Profissional vinculado à clínica com sucesso.")

    def desvincular_profissional(self):
        id_clinica = self.__tela.obter_inteiro("ID da clínica: ")
        clinica = self.__dao.buscar_por_identificador(id_clinica)
        if not clinica:
            self.__tela.exibir_mensagem("Clínica não encontrada.")
            return
        id_prof = self.__tela.obter_id_profissional()
        profissional = self.__dao_profissional.buscar_por_identificador(id_prof)
        if not profissional:
            self.__tela.exibir_mensagem("Profissional não encontrado.")
            return
        clinica.remover_profissional(profissional.identificador)
        if clinica.identificador in profissional.clinicas_associadas:
            profissional.clinicas_associadas.remove(clinica.identificador)
        self.__tela.exibir_mensagem("Profissional desvinculado da clínica.")

    def vincular_tipo_atendimento(self):
        id_clinica = self.__tela.obter_inteiro("ID da clínica: ")
        clinica = self.__dao.buscar_por_identificador(id_clinica)
        if not clinica:
            self.__tela.exibir_mensagem("Clínica não encontrada.")
            return
        id_tipo = self.__tela.obter_id_tipo_atendimento()
        tipo = self.__dao_tipo_atendimento.buscar_por_identificador(id_tipo)
        if not tipo:
            self.__tela.exibir_mensagem("Tipo de atendimento não encontrado.")
            return
        clinica.adicionar_tipo_atendimento(tipo.identificador)
        self.__tela.exibir_mensagem("Tipo de atendimento vinculado à clínica.")

    def desvincular_tipo_atendimento(self):
        id_clinica = self.__tela.obter_inteiro("ID da clínica: ")
        clinica = self.__dao.buscar_por_identificador(id_clinica)
        if not clinica:
            self.__tela.exibir_mensagem("Clínica não encontrada.")
            return
        id_tipo = self.__tela.obter_id_tipo_atendimento()
        tipo = self.__dao_tipo_atendimento.buscar_por_identificador(id_tipo)
        if not tipo:
            self.__tela.exibir_mensagem("Tipo de atendimento não encontrado.")
            return
        clinica.remover_tipo_atendimento(tipo.identificador)
        self.__tela.exibir_mensagem("Tipo de atendimento desvinculado da clínica.")