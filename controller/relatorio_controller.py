class RelatorioController:
    def __init__(self, clinica_dao, atendimento_dao, procedimento_dao, tela):
        self.__clinica_dao = clinica_dao
        self.__atendimento_dao = atendimento_dao
        self.__procedimento_dao = procedimento_dao
        self.__tela = tela

    def ranking_clinicas_atendimentos(self):
        contagem = {}
        for atend in self.__atendimento_dao.listar_todos():
            cid = atend.clinica_identificador
            contagem[cid] = contagem.get(cid, 0) + 1
        ranking = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        self.__tela.mostrar_ranking(ranking, self.__clinica_dao)

    def atendimentos_mais_caro_barato(self):
        data_inicio, data_fim = self.__tela.obter_periodo()
        atendimentos_periodo = [a for a in self.__atendimento_dao.listar_todos() if data_inicio <= a.data <= data_fim]
        if not atendimentos_periodo:
            self.__tela.exibir_mensagem("Nenhum atendimento no período.")
            return
        mais_caro = max(atendimentos_periodo, key=lambda a: a.valor_total)
        mais_barato = min(atendimentos_periodo, key=lambda a: a.valor_total)
        self.__tela.mostrar_atendimentos_extremos(mais_caro, mais_barato)

    def procedimentos_mais_realizados(self):
        contagem = {}
        for atend in self.__atendimento_dao.listar_todos():
            for proc_real in atend.procedimentos_realizados:
                pid = proc_real.procedimento_identificador
                contagem[pid] = contagem.get(pid, 0) + 1
        ordenado = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        self.__tela.mostrar_ranking_procedimentos(ordenado, self.__procedimento_dao)

    def procedimentos_mais_caro_barato_catalogo(self):
        procs = self.__procedimento_dao.listar_todos()
        if not procs:
            self.__tela.exibir_mensagem("Nenhum procedimento cadastrado.")
            return
        mais_caro = max(procs, key=lambda p: p.preco)
        mais_barato = min(procs, key=lambda p: p.preco)
        self.__tela.mostrar_procedimentos_extremos(mais_caro, mais_barato)