"""
Script para popular o banco de dados com anúncios de exemplo
Execute: python3 manage.py shell < popular_anuncios.py
"""

from django.contrib.auth.models import User
from anuncios.models import AnuncioCarro
from decimal import Decimal

# Pegar ou criar um usuário para os anúncios
usuario, created = User.objects.get_or_create(
    username='admin',
    defaults={'is_staff': True, 'is_superuser': True}
)

if created:
    usuario.set_password('admin123')
    usuario.save()
    print(f"Usuário '{usuario.username}' criado!")

# Dados de exemplo
anuncios_exemplo = [
    {
        'titulo': 'Honda HR-V EXL 2023 - Impecável',
        'descricao': 'Honda HR-V EXL 2023 em estado de zero km. Único dono, todas as revisões em dia na concessionária. Carro muito econômico e confortável.',
        'marca': 'HONDA',
        'modelo': 'HR-V EXL',
        'ano': 2023,
        'km': 15000,
        'cambio': 'CVT',
        'combustivel': 'Flex',
        'preco': Decimal('145000.00'),
        'cor': 'Prata',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'status': 'ativo'
    },
    {
        'titulo': 'Volkswagen T-Cross Comfortline 2022',
        'descricao': 'SUV compacto, perfeito para a cidade. Excelente estado de conservação, motor 1.0 TSI turbo muito econômico.',
        'marca': 'VOLKSWAGEN',
        'modelo': 'T-Cross Comfortline',
        'ano': 2022,
        'km': 28000,
        'cambio': 'Automático',
        'combustivel': 'Flex',
        'preco': Decimal('98000.00'),
        'cor': 'Branco',
        'cidade': 'Rio de Janeiro',
        'estado': 'RJ',
        'status': 'ativo'
    },
    {
        'titulo': 'Chevrolet Onix Plus Premier 2024',
        'descricao': 'Sedã moderno com ótimo espaço interno. Equipado com multimídia, ar digital, bancos de couro. Como novo!',
        'marca': 'CHEVROLET',
        'modelo': 'Onix Plus Premier',
        'ano': 2024,
        'km': 5000,
        'cambio': 'Automático',
        'combustivel': 'Flex',
        'preco': Decimal('92000.00'),
        'cor': 'Preto',
        'cidade': 'Belo Horizonte',
        'estado': 'MG',
        'status': 'ativo'
    },
    {
        'titulo': 'Fiat Argo Trekking 2023',
        'descricao': 'Hatch aventureiro com design diferenciado. Motor 1.3 econômico, rodas de liga leve, central multimídia.',
        'marca': 'FIAT',
        'modelo': 'Argo Trekking',
        'ano': 2023,
        'km': 12000,
        'cambio': 'Manual',
        'combustivel': 'Flex',
        'preco': Decimal('72000.00'),
        'cor': 'Vermelho',
        'cidade': 'Curitiba',
        'estado': 'PR',
        'status': 'ativo'
    },
    {
        'titulo': 'Hyundai Creta Limited 2023',
        'descricao': 'SUV premium com todos os opcionais. Teto solar, couro, sensor de estacionamento, câmera 360°. Impecável!',
        'marca': 'HYUNDAI',
        'modelo': 'Creta Limited',
        'ano': 2023,
        'km': 18000,
        'cambio': 'Automático',
        'combustivel': 'Flex',
        'preco': Decimal('135000.00'),
        'cor': 'Cinza',
        'cidade': 'Porto Alegre',
        'estado': 'RS',
        'status': 'ativo'
    },
    {
        'titulo': 'Ford Ranger XLT 2022 - 4x4 Diesel',
        'descricao': 'Picape robusta, ideal para trabalho e lazer. Motor diesel 2.2, tração 4x4, cabine dupla. Aceito troca!',
        'marca': 'FORD',
        'modelo': 'Ranger XLT',
        'ano': 2022,
        'km': 45000,
        'cambio': 'Automático',
        'combustivel': 'Diesel',
        'preco': Decimal('198000.00'),
        'cor': 'Branco',
        'cidade': 'Brasília',
        'estado': 'DF',
        'status': 'ativo'
    },
]

# Criar anúncios
contador = 0
for dados in anuncios_exemplo:
    anuncio, created = AnuncioCarro.objects.get_or_create(
        titulo=dados['titulo'],
        defaults={**dados, 'usuario': usuario}
    )
    
    if created:
        contador += 1
        print(f"✓ Anúncio criado: {anuncio.titulo}")
    else:
        print(f"- Anúncio já existe: {anuncio.titulo}")

print(f"\nTotal de {contador} novo(s) anúncio(s) criado(s)!")
print(f"Total de anúncios no sistema: {AnuncioCarro.objects.count()}")
