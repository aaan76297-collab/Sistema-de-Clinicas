from .view import View

class TelaProcedimento(View):
    def menu_crud(self):
        print("\n--- Gerenciar Procedimentos ---")
        print("1. Adicionar")
        print("2. Pesquisar")
        print("3. Listar todos")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def formulario_adicionar(self):
        print("\n--- Adicionar Procedimento ---")
        descricao = self.obter_texto("Descrição: ")
        duracao = self.obter_inteiro("Duração (min): ", minimo=1)
        preco = self.obter_float("Preço: R$ ", positivo=True)
        return descricao, duracao, preco

    def formulario_pesquisar(self):
        print("\n1. Por ID\n2. Por descrição")
        opcao = self.obter_opcao("Escolha: ", ['1','2'])
        if opcao == '1':
            return 'id', self.obter_inteiro("ID: ")
        else:
            return 'descricao', self.obter_texto("Descrição (ou parte): ")

    def mostrar_procedimento(self, procedimento):
        if procedimento:
            print("\nDetalhes do Procedimento:")
            print(procedimento)
        else:
            print("Procedimento não encontrado.")

    def mostrar_lista(self, lista):
        print("\nProcedimentos:")
        if not lista:
            print("Nenhum procedimento cadastrado.")
        for proc in lista:
            print(proc)

    def formulario_editar(self, procedimento):
        self.mostrar_procedimento(procedimento)
        if not self.confirmar("Deseja editar este procedimento?"):
            return None
        print("Deixe em branco para manter o valor atual.")
        descricao = self.obter_texto(f"Descrição [{procedimento.descricao}]: ", obrigatorio=False)
        if descricao: procedimento.descricao = descricao
        duracao_str = self.obter_texto(f"Duração [{procedimento.duracao}]: ", obrigatorio=False)
        if duracao_str:
            try:
                procedimento.duracao = int(duracao_str)
            except ValueError:
                print("Duração inválida, mantida anterior.")
        preco_str = self.obter_texto(f"Preço [{procedimento.preco:.2f}]: ", obrigatorio=False)
        if preco_str:
            try:
                procedimento.preco = float(preco_str)
            except ValueError:
                print("Preço inválido, mantido anterior.")
        return procedimento

    def confirmar_remocao(self, procedimento):
        self.mostrar_procedimento(procedimento)
        return self.confirmar("Tem certeza que deseja remover este procedimento?")