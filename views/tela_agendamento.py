from .view import View

class TelaAgendamento(View):
    def mostrar_lista_pacientes(self, pacientes):
        print("\nPacientes disponíveis:")
        for paciente in pacientes:
            print(paciente)

    def mostrar_lista_clinicas(self, clinicas):
        print("\nClínicas disponíveis:")
        for clinica in clinicas:
            print(clinica)

    def mostrar_lista_especialidades(self, especialidades):
        print("\nEspecialidades disponíveis:")
        for especialidade in especialidades:
            print(especialidade)

    def mostrar_lista_profissionais(self, profissionais):
        print("\nProfissionais disponíveis:")
        for profissional in profissionais:
            print(profissional)

    def mostrar_lista_tipos_atendimento(self, tipos):
        print("\nTipos de atendimento disponíveis:")
        for tipo in tipos:
            print(tipo)