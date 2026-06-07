from .view import View

class TelaPaciente(View):
    def menu_crud(self):
        print("\n--- Gerenciar Pacientes ---")
        print("1. Adicionar")
        print("2. Pesquisar")
        print("3. Listar todos")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def formulario_adicionar(self):
        print("\n--- Adicionar Paciente ---")
        nome = self.obter_texto("Nome: ")
        cpf = self.obter_cpf("CPF: ")
        data_nasc = self.obter_data("Data de nascimento")
        telefone = self.obter_texto("Telefone: ")
        email = self.obter_texto("E-mail: ")
        return nome, cpf, data_nasc, telefone, email

    def formulario_pesquisar(self):
        print("\n1. Por ID\n2. Por nome\n3. Por CPF")
        opcao = self.obter_opcao("Escolha: ", ['1','2','3'])
        if opcao == '1':
            return 'id', self.obter_inteiro("ID: ")
        elif opcao == '2':
            return 'nome', self.obter_texto("Nome (ou parte): ")
        else:
            return 'cpf', self.obter_cpf("CPF: ")

    def mostrar_paciente(self, paciente):
        if paciente:
            print("\nDetalhes do Paciente:")
            print(paciente)
        else:
            print("Paciente não encontrado.")

    def mostrar_lista(self, lista):
        print("\nPacientes:")
        if not lista:
            print("Nenhum paciente cadastrado.")
        for paciente in lista:
            print(paciente)

    def formulario_editar(self, paciente):
        self.mostrar_paciente(paciente)
        if not self.confirmar("Deseja editar este paciente?"):
            return None
        print("Deixe em branco para manter o valor atual.")
        nome = self.obter_texto(f"Nome [{paciente.nome}]: ", obrigatorio=False)
        if nome: paciente.nome = nome
        telefone = self.obter_texto(f"Telefone [{paciente.contato.telefone}]: ", obrigatorio=False)
        if telefone: paciente.contato.telefone = telefone
        email = self.obter_texto(f"E-mail [{paciente.contato.email}]: ", obrigatorio=False)
        if email: paciente.contato.email = email
        return paciente

    def confirmar_remocao(self, paciente):
        self.mostrar_paciente(paciente)
        return self.confirmar("Tem certeza que deseja remover este paciente?")