from django.db import models
from datetime import datetime
from sistema.constantes import (
    OPCOES_MARCAS,
    OPCOES_CORES,
    OPCOES_COMBUSTIVEL,
)

class Veiculo(models.Model):
    marca = models.CharField(max_length=20, choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=20, choices=OPCOES_CORES)
    combustivel = models.CharField(max_length=20, choices=OPCOES_COMBUSTIVEL)
    foto = models.ImageField(upload_to='veiculos/', blank=True, null=True, help_text='Foto do veículo')
    
    @property
    def veiculo_novo(self):
        return self.ano == datetime.now().year
    def anos_de_uso(self):
        return datetime.now().year - self.ano
        
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.ano}"