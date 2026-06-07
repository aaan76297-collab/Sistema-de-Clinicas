from datetime import date, time, datetime

class View:
    def exibir_mensagem(self, mensagem):
        print(mensagem)

    def obter_opcao(self, mensagem, opcoes_validas):
        while True:
            valor = input(mensagem).strip()
            if valor in opcoes_validas:
                return valor
            print(f"Opção inválida. Digite: {', '.join(opcoes_validas)}")

    def obter_texto(self, mensagem, obrigatorio=True):
        while True:
            valor = input(mensagem).strip()
            if not obrigatorio or valor:
                return valor
            print("Campo obrigatório. Digite novamente.")

    def obter_inteiro(self, mensagem, minimo=None, maximo=None):
        while True:
            try:
                valor = int(input(mensagem))
                if (minimo is None or valor >= minimo) and (maximo is None or valor <= maximo):
                    return valor
                print(f"Valor deve estar entre {minimo} e {maximo}.")
            except ValueError:
                print("Digite um número inteiro válido.")

    def obter_float(self, mensagem, positivo=False):
        while True:
            try:
                valor = float(input(mensagem))
                if not positivo or valor > 0:
                    return valor
                print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um número válido.")

    def obter_data(self, mensagem):
        while True:
            texto = input(mensagem + " (DD/MM/AAAA): ").strip()
            try:
                return datetime.strptime(texto, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")

    def obter_hora(self, mensagem):
        while True:
            texto = input(mensagem + " (HH:MM): ").strip()
            try:
                return datetime.strptime(texto, "%H:%M").time()
            except ValueError:
                print("Hora inválida. Use o formato HH:MM (ex: 14:30).")

    def obter_cpf(self, mensagem):
        while True:
            cpf = input(mensagem).strip()
            if cpf:
                return cpf
            print("CPF não pode ser vazio.")

    def confirmar(self, mensagem):
        resposta = input(mensagem + " (S/N): ").strip().upper()
        return resposta == "S"

    def pausa(self):
        input("Pressione ENTER para continuar...")