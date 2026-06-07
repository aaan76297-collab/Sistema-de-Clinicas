from .view import View

class TelaClinica(View):
    def menu_crud(self):
        print("\n--- Gerenciar Clínicas ---")
        print("1. Adicionar")
        print("2. Pesquisar")
        print("3. Listar todas")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def formulario_adicionar(self):
        print("\n--- Adicionar Clínica ---")
        nome = self.obter_texto("Nome: ")
        localizacao = self.obter_texto("Localização: ")
        descricao = self.obter_texto("Descrição: ")
        abertura = self.obter_hora("Horário de abertura")
        fechamento = self.obter_hora("Horário de fechamento")
        dias_str = self.obter_texto("Dias de funcionamento (0=Seg..6=Dom, separados por vírgula): ")
        dias = [int(d.strip()) for d in dias_str.split(",") if d.strip().isdigit()]
        telefone = self.obter_texto("Telefone: ")
        email = self.obter_texto("E-mail: ")
        return nome, localizacao, descricao, abertura, fechamento, dias, telefone, email

    def formulario_pesquisar(self):
        print("\n1. Por ID\n2. Por nome")
        opcao = self.obter_opcao("Escolha: ", ['1','2'])
        if opcao == '1':
            return 'id', self.obter_inteiro("ID: ")
        else:
            return 'nome', self.obter_texto("Nome (ou parte): ")

    def mostrar_clinica(self, clinica):
        if clinica:
            print("\nDetalhes da Clínica:")
            print(clinica)
        else:
            print("Clínica não encontrada.")

    def mostrar_lista(self, lista):
        print("\nClínicas:")
        if not lista:
            print("Nenhuma clínica cadastrada.")
        for clinica in lista:
            print(clinica)

    def formulario_editar(self, clinica):
        self.mostrar_clinica(clinica)
        if not self.confirmar("Deseja editar esta clínica?"):
            return None
        print("Deixe em branco para manter o valor atual.")
        nome = self.obter_texto(f"Nome [{clinica.nome}]: ", obrigatorio=False)
        if nome: clinica.nome = nome
        localizacao = self.obter_texto(f"Localização [{clinica.localizacao}]: ", obrigatorio=False)
        if localizacao: clinica.localizacao = localizacao
        descricao = self.obter_texto(f"Descrição [{clinica.descricao}]: ", obrigatorio=False)
        if descricao: clinica.descricao = descricao
        telefone = self.obter_texto(f"Telefone [{clinica.contato.telefone}]: ", obrigatorio=False)
        if telefone: clinica.contato.telefone = telefone
        email = self.obter_texto(f"E-mail [{clinica.contato.email}]: ", obrigatorio=False)
        if email: clinica.contato.email = email
        return clinica

    def confirmar_remocao(self, clinica):
        self.mostrar_clinica(clinica)
        return self.confirmar("Tem certeza que deseja remover esta clínica?")