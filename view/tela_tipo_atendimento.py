from .view import View

class TelaTipoAtendimento(View):
    def menu_crud(self):
        print("\n--- Gerenciar Tipos de Atendimento ---")
        print("1. Adicionar")
        print("2. Pesquisar")
        print("3. Listar todos")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def formulario_adicionar(self):
        print("\n--- Adicionar Tipo de Atendimento ---")
        nome = self.obter_texto("Nome: ")
        descricao = self.obter_texto("Descrição: ")
        duracao = self.obter_inteiro("Duração máxima (minutos): ", minimo=1)
        return nome, descricao, duracao

    def formulario_pesquisar(self):
        print("\n1. Por ID\n2. Por nome")
        opcao = self.obter_opcao("Escolha: ", ['1','2'])
        if opcao == '1':
            return 'id', self.obter_inteiro("ID: ")
        else:
            return 'nome', self.obter_texto("Nome (ou parte): ")

    def mostrar_tipo(self, tipo):
        if tipo:
            print("\nDetalhes do Tipo de Atendimento:")
            print(tipo)
        else:
            print("Tipo de atendimento não encontrado.")

    def mostrar_lista(self, lista):
        print("\nTipos de Atendimento:")
        if not lista:
            print("Nenhum tipo cadastrado.")
        for tipo in lista:
            print(tipo)

    def formulario_editar(self, tipo):
        self.mostrar_tipo(tipo)
        if not self.confirmar("Deseja editar este tipo?"):
            return None
        print("Deixe em branco para manter o valor atual.")
        nome = self.obter_texto(f"Nome [{tipo.nome}]: ", obrigatorio=False)
        if nome: tipo.nome = nome
        descricao = self.obter_texto(f"Descrição [{tipo.descricao}]: ", obrigatorio=False)
        if descricao: tipo.descricao = descricao
        duracao_str = self.obter_texto(f"Duração máxima [{tipo.duracao_maxima}]: ", obrigatorio=False)
        if duracao_str:
            try:
                tipo.duracao_maxima = int(duracao_str)
            except ValueError:
                print("Duração inválida, mantida anterior.")
        return tipo

    def confirmar_remocao(self, tipo):
        self.mostrar_tipo(tipo)
        return self.confirmar("Tem certeza que deseja remover este tipo?")