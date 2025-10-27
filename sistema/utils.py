"""
Utilitários compartilhados para formatação de dados
"""

def formatar_preco(valor):
    """Formata um valor decimal para o formato brasileiro de moeda"""
    if valor is None:
        return 'R$ 0,00'
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def formatar_quilometragem(km):
    """Formata a quilometragem com separador de milhar"""
    if km is None:
        return '0 km'
    return f"{km:,} km".replace(',', '.')
