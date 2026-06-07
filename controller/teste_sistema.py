# para testar o sistema
from datetime import date, time, timedelta, datetime
from sistema_controller import SistemaController

def popular_sistema(sistema):
    gerador = sistema._SistemaController__gerador_id
    dao_clinica = sistema._SistemaController__dao_clinica
    dao_paciente = sistema._SistemaController__dao_paciente
    dao_profissional = sistema._SistemaController__dao_profissional
    dao_tipo_atendimento = sistema._SistemaController__dao_tipo_atendimento
    dao_especialidade = sistema._SistemaController__dao_especialidade
    dao_procedimento = sistema._SistemaController__dao_procedimento
    dao_atendimento = sistema._SistemaController__dao_atendimento
    dao_pagamento = sistema._SistemaController__dao_pagamento

    from model.contato import Contato
    from model.clinica import Clinica
    from model.paciente import Paciente
    from model.profissional import Profissional
    from model.especialidade import Especialidade
    from model.tipo_atendimento import TipoAtendimento
    from model.procedimento import Procedimento
    from model.atendimento import Atendimento
    from model.pagamento import PagamentoDinheiro, PagamentoPix, PagamentoCartao

    esp1 = Especialidade(gerador.proximo_id('especialidade'), "Cardiologia", "Coração e vasos")
    esp2 = Especialidade(gerador.proximo_id('especialidade'), "Dermatologia", "Pele e anexos")
    esp3 = Especialidade(gerador.proximo_id('especialidade'), "Ortopedia", "Ossos e articulações")
    esp4 = Especialidade(gerador.proximo_id('especialidade'), "Pediatria", "Saúde infantil")
    dao_especialidade.adicionar(esp1)
    dao_especialidade.adicionar(esp2)
    dao_especialidade.adicionar(esp3)
    dao_especialidade.adicionar(esp4)

    tipo1 = TipoAtendimento(gerador.proximo_id('tipo_atendimento'), "Consulta", "Rotina", 30)
    tipo2 = TipoAtendimento(gerador.proximo_id('tipo_atendimento'), "Exame", "Laboratorial/imagem", 60)
    tipo3 = TipoAtendimento(gerador.proximo_id('tipo_atendimento'), "Emergência", "Urgência/emergência", 120)
    dao_tipo_atendimento.adicionar(tipo1)
    dao_tipo_atendimento.adicionar(tipo2)
    dao_tipo_atendimento.adicionar(tipo3)

    proc1 = Procedimento(gerador.proximo_id('procedimento'), "Eletrocardiograma", 20, 150.0)
    proc2 = Procedimento(gerador.proximo_id('procedimento'), "Raio-X", 15, 80.0)
    proc3 = Procedimento(gerador.proximo_id('procedimento'), "Sutura simples", 30, 200.0)
    proc4 = Procedimento(gerador.proximo_id('procedimento'), "Limpeza de pele", 45, 120.0)
    dao_procedimento.adicionar(proc1)
    dao_procedimento.adicionar(proc2)
    dao_procedimento.adicionar(proc3)
    dao_procedimento.adicionar(proc4)

    clinica1 = Clinica(
        gerador.proximo_id('clinica'),
        "Clínica Bem-Estar",
        "Rua da Saúde, 100",
        "Clínica geral com várias especialidades",
        time(8, 0), time(18, 0),
        [0, 1, 2, 3, 4, 5],  # seg a sáb
        Contato("(11) 3333-1111", "bemestar@clinicas.com")
    )
    clinica1.adicionar_tipo_atendimento(tipo1.identificador)
    clinica1.adicionar_tipo_atendimento(tipo2.identificador)
    clinica1.adicionar_tipo_atendimento(tipo3.identificador)

    clinica2 = Clinica(
        gerador.proximo_id('clinica'),
        "Centro Médico Vida",
        "Av. Central, 500",
        "Foco em ortopedia e reabilitação",
        time(7, 0), time(19, 0),
        [0, 1, 2, 3, 4],  # seg a sex
        Contato("(11) 4444-2222", "contato@vidamed.com")
    )
    clinica2.adicionar_tipo_atendimento(tipo1.identificador)
    clinica2.adicionar_tipo_atendimento(tipo2.identificador)

    clinica3 = Clinica(
        gerador.proximo_id('clinica'),
        "Policlínica Infantil",
        "Rua das Crianças, 300",
        "Especializada em pediatria",
        time(9, 0), time(17, 0),
        [0, 1, 2, 3, 4, 5, 6],  # todos os dias
        Contato("(11) 5555-3333", "infantil@clinicas.com")
    )
    clinica3.adicionar_tipo_atendimento(tipo1.identificador)
    clinica3.adicionar_tipo_atendimento(tipo3.identificador)

    dao_clinica.adicionar(clinica1)
    dao_clinica.adicionar(clinica2)
    dao_clinica.adicionar(clinica3)

    pac1 = Paciente(gerador.proximo_id('paciente'), "João Silva",
                    Contato("(11) 98888-0001", "joao@email.com"), "123.456.789-00",
                    date(1990, 5, 20))
    pac2 = Paciente(gerador.proximo_id('paciente'), "Maria Santos",
                    Contato("(11) 97777-0002", "maria@email.com"), "987.654.321-00",
                    date(1985, 11, 15))
    pac3 = Paciente(gerador.proximo_id('paciente'), "Carlos Júnior",
                    Contato("(11) 96666-0003", "carlos@email.com"), "111.222.333-44",
                    date(2008, 3, 10))  # menor de idade
    pac4 = Paciente(gerador.proximo_id('paciente'), "Ana Beatriz",
                    Contato("(11) 95555-0004", "ana@email.com"), "222.333.444-55",
                    date(1995, 7, 25))
    pac5 = Paciente(gerador.proximo_id('paciente'), "Pedro Alves",
                    Contato("(11) 94444-0005", "pedro@email.com"), "333.444.555-66",
                    date(2000, 1, 10))
    dao_paciente.adicionar(pac1)
    dao_paciente.adicionar(pac2)
    dao_paciente.adicionar(pac3)
    dao_paciente.adicionar(pac4)
    dao_paciente.adicionar(pac5)

    prof1 = Profissional(gerador.proximo_id('profissional'), "Dr. Ricardo Cardoso",
                         Contato("(11) 95555-1111", "ricardo@med.com"), "444.555.666-77",
                         "CRM-SP 12345", esp1.identificador,
                         [0, 1, 2, 3, 4], time(8, 0), time(17, 0))
    prof1.adicionar_clinica(clinica1.identificador)
    prof2 = Profissional(gerador.proximo_id('profissional'), "Dra. Ana Dermatologista",
                         Contato("(11) 94444-2222", "ana@med.com"), "555.666.777-88",
                         "CRM-SP 67890", esp2.identificador,
                         [0, 1, 2, 3, 4, 5], time(9, 0), time(18, 0))
    prof2.adicionar_clinica(clinica1.identificador)
    prof3 = Profissional(gerador.proximo_id('profissional'), "Dr. Paulo Ortopedista",
                         Contato("(11) 93333-3333", "paulo@med.com"), "666.777.888-99",
                         "CRM-SP 11223", esp3.identificador,
                         [0, 1, 2, 3, 4], time(7, 0), time(16, 0))
    prof3.adicionar_clinica(clinica2.identificador)
    prof4 = Profissional(gerador.proximo_id('profissional'), "Dra. Lúcia Pediatra",
                         Contato("(11) 92222-4444", "lucia@med.com"), "777.888.999-00",
                         "CRM-SP 44556", esp4.identificador,
                         [0, 1, 2, 3, 4, 5, 6], time(9, 0), time(17, 0))
    prof4.adicionar_clinica(clinica3.identificador)
    dao_profissional.adicionar(prof1)
    dao_profissional.adicionar(prof2)
    dao_profissional.adicionar(prof3)
    dao_profissional.adicionar(prof4)

    clinica1.adicionar_profissional(prof1.identificador)
    clinica1.adicionar_profissional(prof2.identificador)
    clinica2.adicionar_profissional(prof3.identificador)
    clinica3.adicionar_profissional(prof4.identificador)

    hoje = date.today()
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    data1 = inicio_semana
    atend1 = Atendimento(gerador.proximo_id('atendimento'), clinica1.identificador, pac1.identificador,
                         prof1.identificador, tipo1.identificador, esp1.identificador,
                         data1, time(9, 0), time(9, 30), 200.0, "atendimento realizado")
    dao_atendimento.adicionar(atend1)
    clinica1.adicionar_atendimento(atend1.identificador)
    pac1.adicionar_atendimento(atend1.identificador)
    prof1.adicionar_atendimento(atend1.identificador)
    pag1 = PagamentoDinheiro(gerador.proximo_id('pagamento'), data1, time(9, 30), 200.0)
    atend1.adicionar_pagamento(pag1)
    dao_pagamento.adicionar(pag1)

    data2 = inicio_semana + timedelta(days=1)
    atend2 = Atendimento(gerador.proximo_id('atendimento'), clinica1.identificador, pac2.identificador,
                         prof2.identificador, tipo2.identificador, esp2.identificador,
                         data2, time(10, 0), time(11, 0), 150.0, "agendado")
    dao_atendimento.adicionar(atend2)
    clinica1.adicionar_atendimento(atend2.identificador)
    pac2.adicionar_atendimento(atend2.identificador)
    prof2.adicionar_atendimento(atend2.identificador)

    data3 = inicio_semana + timedelta(days=2)
    atend3 = Atendimento(gerador.proximo_id('atendimento'), clinica2.identificador, pac4.identificador,
                         prof3.identificador, tipo1.identificador, esp3.identificador,
                         data3, time(8, 0), time(8, 30), 350.0, "confirmado")
    dao_atendimento.adicionar(atend3)
    clinica2.adicionar_atendimento(atend3.identificador)
    pac4.adicionar_atendimento(atend3.identificador)
    prof3.adicionar_atendimento(atend3.identificador)
    pag3 = PagamentoCartao(gerador.proximo_id('pagamento'), data3, time(9, 0), 350.0,
                           "Visa", "1234.5678.9012.3456", "credito", 3)
    atend3.adicionar_pagamento(pag3)
    dao_pagamento.adicionar(pag3)

    data4 = inicio_semana + timedelta(days=3)
    atend4 = Atendimento(gerador.proximo_id('atendimento'), clinica3.identificador, pac5.identificador,
                         prof4.identificador, tipo3.identificador, esp4.identificador,
                         data4, time(9, 0), time(11, 0), 120.0, "agendado")
    dao_atendimento.adicionar(atend4)
    clinica3.adicionar_atendimento(atend4.identificador)
    pac5.adicionar_atendimento(atend4.identificador)
    prof4.adicionar_atendimento(atend4.identificador)

    data5 = inicio_semana + timedelta(days=4)
    atend5 = Atendimento(gerador.proximo_id('atendimento'), clinica1.identificador, pac1.identificador,
                         prof1.identificador, tipo2.identificador, esp1.identificador,
                         data5, time(10, 0), time(11, 0), 180.0, "agendado")
    dao_atendimento.adicionar(atend5)
    clinica1.adicionar_atendimento(atend5.identificador)
    pac1.adicionar_atendimento(atend5.identificador)
    prof1.adicionar_atendimento(atend5.identificador)
    pag5 = PagamentoPix(gerador.proximo_id('pagamento'), data5, time(11, 0), 180.0,
                        "João Silva", "fisica", "123.456.789-00")
    atend5.adicionar_pagamento(pag5)
    dao_pagamento.adicionar(pag5)

    print("\nDados de teste:")
    print(f"Clínicas: {len(dao_clinica.listar_todos())}")
    print(f"Pacientes: {len(dao_paciente.listar_todos())}")
    print(f"Profissionais: {len(dao_profissional.listar_todos())}")
    print(f"Atendimentos: {len(dao_atendimento.listar_todos())}")
    print(f"Pagamentos: {len(dao_pagamento.listar_todos())}")


if __name__ == "__main__":
    sistema = SistemaController()
    popular_sistema(sistema)
    print("\nIniciando sistema interativo...\n")
    sistema.executar()