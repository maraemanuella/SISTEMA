"""
Utilitários compartilhados para formatação de dados
"""

def formatar_preco(valor):
    """Formata um valor decimal para o formato brasileiro de moeda"""
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def formatar_quilometragem(km):
    """Formata a quilometragem com separador de milhar"""
    return f"{km:,} km".replace(',', '.')
