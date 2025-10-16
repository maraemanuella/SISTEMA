"""
Constantes compartilhadas entre os apps do sistema
"""

# Marcas de veículos
OPCOES_MARCAS = (
    ('AUDI', 'Audi'),
    ('BMW', 'BMW'),
    ('CHEVROLET', 'Chevrolet'),
    ('FERRARI', 'Ferrari'),
    ('FIAT', 'Fiat'),
    ('FORD', 'Ford'),
    ('HONDA', 'Honda'),
    ('HYUNDAI', 'Hyundai'),
    ('VOLKSWAGEN', 'Volkswagen'),
)

# Tipos de combustível
OPCOES_COMBUSTIVEL = (
    ('Gasolina', 'Gasolina'),
    ('Etanol', 'Etanol'),
    ('Flex', 'Flex'),
    ('Diesel', 'Diesel'),
    ('Híbrido', 'Híbrido'),
    ('Elétrico', 'Elétrico'),
)

# Tipos de câmbio
OPCOES_CAMBIO = (
    ('Manual', 'Manual'),
    ('Automático', 'Automático'),
    ('CVT', 'CVT'),
)

# Status de anúncios
OPCOES_STATUS = (
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
    ('vendido', 'Vendido'),
)

# Cores de veículos
OPCOES_CORES = (
    ('Vermelho', 'Vermelho'),
    ('Branco', 'Branco'),
    ('Azul', 'Azul'),
    ('Preto', 'Preto'),
    ('Cinza', 'Cinza'),
    ('Prata', 'Prata'),
)

# Estados brasileiros
OPCOES_ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

# Opções de ordenação
OPCOES_ORDENACAO = (
    ('-data_publicacao', 'Mais Recentes'),
    ('data_publicacao', 'Mais Antigos'),
    ('preco', 'Menor Preço'),
    ('-preco', 'Maior Preço'),
    ('km', 'Menor KM'),
    ('-km', 'Maior KM'),
)
