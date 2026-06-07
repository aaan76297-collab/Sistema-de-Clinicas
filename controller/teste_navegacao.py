"""
Script para popular o sistema com dados de teste e iniciar a navegação interativa.
Basta executar: python teste_navegacao.py
"""
from sistema_controller import SistemaController

def main():
    sistema = SistemaController()
    sistema.popular_dados_teste()
    print("\nIniciando sistema interativo...\n")
    sistema.executar()

if __name__ == "__main__":
    main()