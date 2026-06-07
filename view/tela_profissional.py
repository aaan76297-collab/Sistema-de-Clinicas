from .view import View
from model.especialidade import Especialidade

class TelaProfissional(View):
    def menu_crud(self):
        print("\n--- Gerenciar Profissionais ---")
        print("1. Adicionar")
        print("2. Pesquisar")
        print("3. Listar todos")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def formulario_adicionar(self):
        print("\n--- Adicionar Profissional ---")
        nome = self.obter_texto("Nome: ")
        cpf = self.obter_cpf("CPF: ")
        registro = self.obter_texto("Registro profissional: ")
        print("\nDias de trabalho (0=Seg, 1=Ter, 2=Qua, 3=Qui, 4=Sex, 5=Sáb, 6=Dom)")
        dias_str = self.obter_texto("Dias (separados por vírgula): ")
        dias_trabalho = [int(d.strip()) for d in dias_str.split(",") if d.strip().isdigit()]
        horario_inicio = self.obter_hora("Horário de início")
        horario_fim = self.obter_hora("Horário de fim")
        telefone = self.obter_texto("Telefone: ")
        email = self.obter_texto("E-mail: ")
        especialidade_id = self.obter_inteiro("ID da especialidade (0 para cadastrar nova): ")
        return nome, cpf, registro, dias_trabalho, horario_inicio, horario_fim, telefone, email, especialidade_id

    def cadastrar_nova_especialidade(self, especialidade_dao):
        nome = self.obter_texto("Nome da nova especialidade: ")
        descricao = self.obter_texto("Descrição: ")
        novo_id = especialidade_dao.proximo_identificador()
        especialidade = Especialidade(novo_id, nome, descricao)
        especialidade_dao.adicionar(especialidade)
        print(f"Especialidade criada com ID {novo_id}.")
        return novo_id

    def formulario_pesquisar(self):
        print("\n1. Por ID\n2. Por nome\n3. Por registro profissional")
        opcao = self.obter_opcao("Escolha: ", ['1','2','3'])
        if opcao == '1':
            return 'id', self.obter_inteiro("ID: ")
        elif opcao == '2':
            return 'nome', self.obter_texto("Nome (ou parte): ")
        else:
            return 'registro', self.obter_texto("Registro profissional: ")

    def mostrar_profissional(self, profissional):
        if profissional:
            print("\nDetalhes do Profissional:")
            print(profissional)
        else:
            print("Profissional não encontrado.")

    def mostrar_lista(self, lista):
        print("\nProfissionais:")
        if not lista:
            print("Nenhum profissional cadastrado.")
        for profissional in lista:
            print(profissional)

    def formulario_editar(self, profissional):
        self.mostrar_profissional(profissional)
        if not self.confirmar("Deseja editar este profissional?"):
            return None
        print("Deixe em branco para manter o valor atual.")
        nome = self.obter_texto(f"Nome [{profissional.nome}]: ", obrigatorio=False)
        if nome: profissional.nome = nome
        telefone = self.obter_texto(f"Telefone [{profissional.contato.telefone}]: ", obrigatorio=False)
        if telefone: profissional.contato.telefone = telefone
        email = self.obter_texto(f"E-mail [{profissional.contato.email}]: ", obrigatorio=False)
        if email: profissional.contato.email = email
        return profissional

    def confirmar_remocao(self, profissional):
        self.mostrar_profissional(profissional)
        return self.confirmar("Tem certeza que deseja remover este profissional?")