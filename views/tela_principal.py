from .view import View

class TelaPrincipal(View):
    def menu_principal(self):
        print("\n" + "="*50)
        print("SISTEMA DE GERENCIAMENTO DE CLÍNICAS")
        print("="*50)
        print("1. Agendamentos")
        print("2. Cadastros")
        print("3. Navegar")
        print("4. Gerenciar")
        print("5. Relatórios")
        print("0. Encerrar")
        return self.obter_opcao("Escolha uma opção: ", ['0','1','2','3','4','5'])

    def menu_cadastros(self):
        print("\n--- CADASTROS RÁPIDOS ---")
        print("1. Nova Clínica")
        print("2. Novo Paciente")
        print("3. Novo Profissional")
        print("4. Novo Tipo de Atendimento")
        print("5. Nova Especialidade")
        print("6. Novo Procedimento")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5','6'])

    def menu_navegar(self):
        print("\n--- NAVEGAR (Listar / Pesquisar) ---")
        print("1. Clínicas")
        print("2. Pacientes")
        print("3. Profissionais")
        print("4. Tipos de Atendimento")
        print("5. Especialidades")
        print("6. Procedimentos")
        print("7. Atendimentos")
        print("8. Pagamentos")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5','6','7','8'])

    def menu_gerenciar(self):
        print("\n--- GERENCIAR (CRUD Completo) ---")
        print("1. Clínicas")
        print("2. Pacientes")
        print("3. Profissionais")
        print("4. Tipos de Atendimento")
        print("5. Especialidades")
        print("6. Procedimentos")
        print("7. Atendimentos")
        print("8. Pagamentos")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4','5','6','7','8'])

    def menu_relatorios(self):
        print("\n--- RELATÓRIOS ---")
        print("1. Ranking de clínicas por número de atendimentos")
        print("2. Atendimentos mais caro e mais barato (com filtro por período)")
        print("3. Procedimentos mais realizados")
        print("4. Procedimentos mais caros e mais baratos do catálogo")
        print("0. Voltar")
        return self.obter_opcao("Opção: ", ['0','1','2','3','4'])