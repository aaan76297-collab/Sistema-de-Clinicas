from model.pagamento import PagamentoDinheiro, PagamentoPix, PagamentoCartao

class PagamentoController:
    def __init__(self, dao, atendimento_dao, tela):
        self.__dao = dao
        self.__atendimento_dao = atendimento_dao
        self.__tela = tela

    def adicionar(self):
        try:
            id_atendimento, modalidade, dados = self.__tela.formulario_adicionar()
            atendimento = self.__atendimento_dao.buscar_por_identificador(id_atendimento)
            if not atendimento:
                self.__tela.exibir_mensagem("Atendimento não encontrado.")
                return

            data_pagamento = dados['data']
            hora = dados['hora']
            valor = dados['valor']

            if data_pagamento > atendimento.data:
                self.__tela.exibir_mensagem("Erro: Data do pagamento não pode ser posterior à data do atendimento.")
                return

            if modalidade == 'pix':
                if not dados.get('documento'):
                    self.__tela.exibir_mensagem("Erro: CPF/CNPJ do pagador é obrigatório para PIX.")
                    return
            elif modalidade == 'cartao':
                if not dados.get('numero_cartao') or not dados.get('tipo_cartao'):
                    self.__tela.exibir_mensagem("Erro: Número do cartão e bandeira são obrigatórios.")
                    return

            novo_id = self.__dao.proximo_identificador()
            if modalidade == 'dinheiro':
                pagamento = PagamentoDinheiro(novo_id, data_pagamento, hora, valor)
            elif modalidade == 'pix':
                pagamento = PagamentoPix(novo_id, data_pagamento, hora, valor,
                                         dados['nome_pagador'], dados['tipo_pessoa'], dados['documento'])
            elif modalidade == 'cartao':
                pagamento = PagamentoCartao(novo_id, data_pagamento, hora, valor,
                                            dados['tipo_cartao'], dados['numero_cartao'],
                                            dados['modalidade_cartao'], dados['numero_parcelas'])
            else:
                self.__tela.exibir_mensagem("Modalidade inválida.")
                return

            self.__dao.adicionar(pagamento)
            atendimento.adicionar_pagamento(pagamento)
            self.__tela.exibir_mensagem(f"Pagamento ID {novo_id} adicionado ao atendimento.")

        except KeyError as erro:
            self.__tela.exibir_mensagem(f"Erro: campo obrigatório ausente ({erro}).")
        except Exception as erro:
            self.__tela.exibir_mensagem(f"Erro ao registrar pagamento: {erro}")

    def pesquisar(self):
        try:
            identificador = self.__tela.obter_inteiro("ID do pagamento: ")
            pagamento = self.__dao.buscar_por_identificador(identificador)
            self.__tela.mostrar_pagamento(pagamento)
        except Exception as erro:
            self.__tela.exibir_mensagem(f"Erro na pesquisa: {erro}")

    def ver_todos(self):
        self.__tela.mostrar_lista(self.__dao.listar_todos())

    def editar(self):
        self.__tela.exibir_mensagem("Edição de pagamento não implementada nesta versão.")

    def remover(self):
        try:
            identificador = self.__tela.obter_inteiro("ID do pagamento a remover: ")
            pagamento = self.__dao.buscar_por_identificador(identificador)
            if not pagamento:
                self.__tela.exibir_mensagem("Pagamento não encontrado.")
                return
            if self.__tela.confirmar_remocao(pagamento):
                for atendimento in self.__atendimento_dao.listar_todos():
                    if pagamento in atendimento.pagamentos:
                        atendimento.remover_pagamento(pagamento)
                        break
                self.__dao.remover(identificador)
                self.__tela.exibir_mensagem("Pagamento removido.")
        except Exception as erro:
            self.__tela.exibir_mensagem(f"Erro ao remover pagamento: {erro}")