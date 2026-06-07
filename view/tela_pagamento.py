from .view import View

class TelaPagamento(View):
    def menu_crud(self):
        print("\n--- Gerenciar Pagamentos ---")
        print("1. Adicionar pagamento a um atendimento")
        print("2. Pesquisar")
        print("3. Listar todos")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def formulario_adicionar(self):
        print("\n--- Adicionar Pagamento ---")
        id_atendimento = self.obter_inteiro("ID do atendimento: ")
        print("Modalidades: 1 - Dinheiro, 2 - PIX, 3 - Cartão")
        modalidade_op = self.obter_opcao("Escolha: ", ['1','2','3'])
        modalidade = {'1': 'dinheiro', '2': 'pix', '3': 'cartao'}[modalidade_op]
        data_pag = self.obter_data("Data do pagamento")
        hora_pag = self.obter_hora("Hora do pagamento")
        valor = self.obter_float("Valor pago: R$ ", positivo=True)
        dados = {'data': data_pag, 'hora': hora_pag, 'valor': valor}

        if modalidade == 'pix':
            dados['nome_pagador'] = self.obter_texto("Nome do pagador: ")
            dados['tipo_pessoa'] = self.obter_texto("Tipo de pessoa (fisica/juridica): ")
            dados['documento'] = self.obter_cpf("CPF/CNPJ do pagador: ")
        elif modalidade == 'cartao':
            dados['tipo_cartao'] = self.obter_texto("Bandeira do cartão (ex: Visa): ")
            dados['numero_cartao'] = self.obter_texto("Número do cartão: ")
            modalidade_cartao = self.obter_opcao("Modalidade (credito/debito): ", ['credito','debito'])
            dados['modalidade_cartao'] = modalidade_cartao
            if modalidade_cartao == 'credito':
                dados['numero_parcelas'] = self.obter_inteiro("Número de parcelas: ", minimo=1)
            else:
                dados['numero_parcelas'] = 1

        return id_atendimento, modalidade, dados

    def mostrar_pagamento(self, pagamento):
        if pagamento:
            print("\nDetalhes do Pagamento:")
            print(pagamento)
        else:
            print("Pagamento não encontrado.")

    def mostrar_lista(self, lista):
        print("\nPagamentos:")
        if not lista:
            print("Nenhum pagamento cadastrado.")
        for pagamento in lista:
            print(pagamento)

    def confirmar_remocao(self, pagamento):
        self.mostrar_pagamento(pagamento)
        return self.confirmar("Tem certeza que deseja remover este pagamento?")