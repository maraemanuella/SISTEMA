from datetime import datetime

from django.forms import FileInput, ModelForm, NumberInput, Select, TextInput

from veiculo.models import Veiculo


CURRENT_YEAR = datetime.now().year

class FormularioVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'cor', 'combustivel', 'foto']
        widgets = {
            'marca': Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'modelo': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Civic, Corolla, Gol...',
                'required': True
            }),
            'ano': NumberInput(attrs={
                'class': 'form-control',
                'min': 1900,
                'max': CURRENT_YEAR + 1,
                'required': True
            }),
            'cor': Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'combustivel': Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'foto': FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'ano': 'Ano',
            'cor': 'Cor',
            'combustivel': 'Combustível',
            'foto': 'Foto do Veículo',
        }  