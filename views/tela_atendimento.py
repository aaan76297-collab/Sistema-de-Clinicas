from .view import View

class TelaAtendimento(View):
    def menu_crud(self):
        print("\n--- Gerenciar Atendimentos ---")
        print("1. Adicionar (via agendamento)")
        print("2. Pesquisar")
        print("3. Listar todos")
        print("4. Editar")
        print("5. Remover")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5'])

    def mostrar_atendimento(self, atendimento):
        if atendimento:
            print("\nDetalhes do Atendimento:")
            print(atendimento)
            print("Procedimentos realizados:", len(atendimento.procedimentos_realizados))
            print("Pagamentos:", len(atendimento.pagamentos))
        else:
            print("Atendimento não encontrado.")

    def mostrar_lista(self, lista):
        print("\nAtendimentos:")
        if not lista:
            print("Nenhum atendimento cadastrado.")
        for atendimento in lista:
            print(atendimento)

    def formulario_editar(self, atendimento):
        self.mostrar_atendimento(atendimento)
        if not self.confirmar("Deseja editar este atendimento?"):
            return None
        print("Deixe em branco para manter o valor atual.")
        novo_status = self.obter_texto(f"Novo status [{atendimento.status}]: ", obrigatorio=False)
        if novo_status:
            try:
                atendimento.status = novo_status
            except ValueError as erro:
                print(f"Erro: {erro}")
                return None
        return atendimento

    def confirmar_remocao(self, atendimento):
        self.mostrar_atendimento(atendimento)
        return self.confirmar("Tem certeza que deseja remover este atendimento?")