from django.db import models
from veiculo.const import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEL

class Veiculo(models.Model):
    marca = models.CharField(max_length=20, choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=20, choices=OPCOES_CORES)
    combustivel = models.CharField(max_length=20, choices=OPCOES_COMBUSTIVEL)
    foto = models.ImageField(upload_to='veiculos/', blank=True, null=True, help_text='Foto do veículo')
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.ano}"