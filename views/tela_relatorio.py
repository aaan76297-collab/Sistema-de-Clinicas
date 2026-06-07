from .view import View

class TelaRelatorio(View):
    def obter_periodo(self):
        print("\n--- Filtrar por período ---")
        data_inicio = self.obter_data("Data inicial")
        data_fim = self.obter_data("Data final")
        return data_inicio, data_fim

    def mostrar_ranking(self, ranking, clinica_dao):
        print("\n--- Ranking de Clínicas por Nº de Atendimentos ---")
        if not ranking:
            print("Nenhum atendimento registrado.")
        for clinica_id, quantidade in ranking:
            clinica = clinica_dao.buscar_por_identificador(clinica_id)
            nome = clinica.nome if clinica else "Desconhecida"
            print(f"{nome} (ID {clinica_id}): {quantidade} atendimento(s)")

    def mostrar_atendimentos_extremos(self, mais_caro, mais_barato):
        print("\n--- Atendimentos Extremos no Período ---")
        print("Mais caro:")
        print(mais_caro)
        print("Mais barato:")
        print(mais_barato)

    def mostrar_ranking_procedimentos(self, ranking, procedimento_dao):
        print("\n--- Procedimentos Mais Realizados ---")
        if not ranking:
            print("Nenhum procedimento registrado em atendimentos.")
        for proc_id, quantidade in ranking:
            proc = procedimento_dao.buscar_por_identificador(proc_id)
            nome = proc.descricao if proc else f"ID {proc_id}"
            print(f"{nome}: {quantidade} vez(es)")

    def mostrar_procedimentos_extremos(self, mais_caro, mais_barato):
        print("\n--- Procedimentos Extremos do Catálogo ---")
        print("Mais caro:")
        print(mais_caro)
        print("Mais barato:")
        print(mais_barato)