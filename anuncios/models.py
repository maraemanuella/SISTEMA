from django.db import models
from django.contrib.auth.models import User
from sistema.constantes import (
    OPCOES_MARCAS, OPCOES_COMBUSTIVEL, OPCOES_CAMBIO,
    OPCOES_STATUS, OPCOES_ESTADOS, OPCOES_CORES
)
from sistema.utils import formatar_preco, formatar_quilometragem


class AnuncioCarro(models.Model):
    """
    Modelo para representar anúncios de venda de carros.
    
    Este modelo armazena todas as informações necessárias para um anúncio
    de veículo, incluindo dados do carro, preço, localização e imagens.
    
    Attributes:
        titulo (str): Título descritivo do anúncio (máx. 100 caracteres)
        descricao (str): Descrição detalhada do anúncio (opcional)
        status (str): Status do anúncio (ativo, vendido, suspenso)
        marca (str): Marca do veículo (Honda, Toyota, Ford, etc.)
        modelo (str): Modelo do veículo (máx. 50 caracteres)
        ano (int): Ano de fabricação do veículo
        km (int): Quilometragem atual do veículo
        cambio (str): Tipo de câmbio (manual, automático, etc.)
        combustivel (str): Tipo de combustível (gasolina, diesel, flex, etc.)
        preco (Decimal): Preço de venda do veículo (até 12 dígitos)
        cor (str): Cor do veículo (opcional)
        imagem_principal (ImageField): Imagem principal do anúncio
        imagens_adicionais (JSONField): Lista de imagens adicionais
        cidade (str): Cidade onde o veículo está localizado (opcional)
        estado (str): Estado (UF) onde o veículo está localizado (opcional)
        data_publicacao (datetime): Data e hora de criação do anúncio
        usuario (ForeignKey): Usuário que criou o anúncio
    
    Methods:
        get_preco_formatado(): Retorna o preço formatado em moeda brasileira
        get_km_formatado(): Retorna a quilometragem formatada com separador de milhares
    
    Meta:
        ordering: Anúncios mais recentes aparecem primeiro
        db_table: 'anuncios_carros'
    """
    
    # Informações do anúncio
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    status = models.CharField(
        max_length=10, 
        choices=OPCOES_STATUS, 
        default='ativo', 
        verbose_name='Status'
    )
    
    # Informações do veículo
    marca = models.CharField(max_length=50, choices=OPCOES_MARCAS, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    ano = models.IntegerField(verbose_name='Ano')
    km = models.IntegerField(default=0, verbose_name='Quilometragem')
    cambio = models.CharField(max_length=20, choices=OPCOES_CAMBIO, verbose_name='Câmbio')
    combustivel = models.CharField(max_length=20, choices=OPCOES_COMBUSTIVEL, verbose_name='Combustível')
    preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Preço')
    cor = models.CharField(max_length=30, choices=OPCOES_CORES, blank=True, null=True, verbose_name='Cor')
    
    # Imagens
    imagem_principal = models.ImageField(
        upload_to='anuncios/', 
        blank=True, 
        null=True, 
        verbose_name='Imagem Principal'
    )
    imagens_adicionais = models.JSONField(
        blank=True, 
        null=True, 
        verbose_name='Imagens Adicionais'
    )
    
    # Localização
    cidade = models.CharField(max_length=80, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, choices=OPCOES_ESTADOS, blank=True, null=True, verbose_name='Estado')
    
    # Controle
    data_publicacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Publicação')
    usuario = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        verbose_name='Usuário',
        related_name='anuncios'
    )
    
    class Meta:
        db_table = 'anuncios_carros'
        verbose_name = 'Anúncio de Carro'
        verbose_name_plural = 'Anúncios de Carros'
        ordering = ['-data_publicacao']
    
    def __str__(self):
        """Retorna uma representação em string do anúncio."""
        return f"{self.titulo} - {self.marca} {self.modelo} ({self.ano})"
    
    def get_preco_formatado(self):
        """
        Formata o preço do veículo em moeda brasileira.
        
        Returns:
            str: Preço formatado no padrão 'R$ X.XXX,XX'
            
        Example:
            >>> anuncio.preco = 45000.00
            >>> anuncio.get_preco_formatado()
            'R$ 45.000,00'
        """
        return formatar_preco(self.preco)
    
    def get_km_formatado(self):
        """
        Formata a quilometragem com separador de milhares.
        
        Returns:
            str: Quilometragem formatada com ' km' no final
            
        Example:
            >>> anuncio.km = 50000
            >>> anuncio.get_km_formatado()
            '50.000 km'
        """
        return formatar_quilometragem(self.km)
