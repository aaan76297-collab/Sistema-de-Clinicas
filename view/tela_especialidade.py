from .view import View

class TelaEspecialidade(View):
    def menu_crud(self):
        print("\n--- Gerenciar Especialidades ---")
        print("1. Adicionar")
        print("2. Pesquisar")
        print("3. Listar todas")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def formulario_adicionar(self):
        print("\n--- Adicionar Especialidade ---")
        nome = self.obter_texto("Nome: ")
        descricao = self.obter_texto("Descrição: ")
        return nome, descricao

    def formulario_pesquisar(self):
        print("\n1. Por ID\n2. Por nome")
        opcao = self.obter_opcao("Escolha: ", ['1','2'])
        if opcao == '1':
            return 'id', self.obter_inteiro("ID: ")
        else:
            return 'nome', self.obter_texto("Nome (ou parte): ")

    def mostrar_especialidade(self, especialidade):
        if especialidade:
            print("\nDetalhes da Especialidade:")
            print(especialidade)
        else:
            print("Especialidade não encontrada.")

    def mostrar_lista(self, lista):
        print("\nEspecialidades:")
        if not lista:
            print("Nenhuma especialidade cadastrada.")
        for esp in lista:
            print(esp)

    def formulario_editar(self, especialidade):
        self.mostrar_especialidade(especialidade)
        if not self.confirmar("Deseja editar esta especialidade?"):
            return None
        print("Deixe em branco para manter o valor atual.")
        nome = self.obter_texto(f"Nome [{especialidade.nome}]: ", obrigatorio=False)
        if nome: especialidade.nome = nome
        descricao = self.obter_texto(f"Descrição [{especialidade.descricao}]: ", obrigatorio=False)
        if descricao: especialidade.descricao = descricao
        return especialidade

    def confirmar_remocao(self, especialidade):
        self.mostrar_especialidade(especialidade)
        return self.confirmar("Tem certeza que deseja remover esta especialidade?")