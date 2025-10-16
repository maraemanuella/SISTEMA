"""
Formulários para o app de anúncios de carros.
Define validações e widgets para criação e edição de anúncios.
"""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

from anuncios.models import AnuncioCarro


class AnuncioCarroForm(forms.ModelForm):
    """
    Formulário para criar e editar anúncios de carros.
    Inclui validações customizadas e widgets estilizados com Bootstrap.
    """
    
    # Validações personalizadas
    ano = forms.IntegerField(
        validators=[
            MinValueValidator(1900, message='O ano deve ser maior que 1900.'),
            MaxValueValidator(datetime.now().year + 1, message=f'O ano não pode ser maior que {datetime.now().year + 1}.')
        ],
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': f'Ex: {datetime.now().year}',
            'min': 1900,
            'max': datetime.now().year + 1
        })
    )
    
    km = forms.IntegerField(
        validators=[MinValueValidator(0, message='A quilometragem não pode ser negativa.')],
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 15000',
            'min': 0
        })
    )
    
    preco = forms.DecimalField(
        validators=[MinValueValidator(0, message='O preço não pode ser negativo.')],
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 85000.00',
            'step': '0.01',
            'min': 0
        })
    )
    
    class Meta:
        model = AnuncioCarro
        fields = [
            'titulo', 'descricao', 'marca', 'modelo', 'ano', 'km', 
            'cambio', 'combustivel', 'preco', 'cor', 'cidade', 
            'estado', 'imagem_principal'
        ]
        
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Honda HR-V 2023 EXL',
                'maxlength': 100
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Descreva as características e o estado do veículo...'
            }),
            'marca': forms.Select(attrs={
                'class': 'form-select'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: HR-V EXL',
                'maxlength': 50
            }),
            'cambio': forms.Select(attrs={
                'class': 'form-select'
            }),
            'combustivel': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cor': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: São Paulo',
                'maxlength': 80
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'imagem_principal': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/jpeg,image/png,image/gif'
            })
        }
        
        help_texts = {
            'titulo': 'Título atrativo para seu anúncio (máx. 100 caracteres)',
            'descricao': 'Descreva detalhes importantes do veículo',
            'imagem_principal': 'Formatos aceitos: JPG, PNG, GIF. Tamanho máximo: 5MB.',
        }
    
    def clean_ano(self):
        """Valida se o ano está em um range aceitável"""
        ano = self.cleaned_data.get('ano')
        ano_atual = datetime.now().year
        
        if ano and (ano < 1900 or ano > ano_atual + 1):
            raise forms.ValidationError(
                f'O ano deve estar entre 1900 e {ano_atual + 1}.'
            )
        return ano
    
    def clean_preco(self):
        """Valida se o preço é positivo"""
        preco = self.cleaned_data.get('preco')
        if preco and preco <= 0:
            raise forms.ValidationError('O preço deve ser maior que zero.')
        return preco
    
    def clean_km(self):
        """Valida se a quilometragem é válida"""
        km = self.cleaned_data.get('km')
        if km and km < 0:
            raise forms.ValidationError('A quilometragem não pode ser negativa.')
        return km
    
    def clean_imagem_principal(self):
        """Valida tamanho e tipo da imagem"""
        imagem = self.cleaned_data.get('imagem_principal')
        
        if imagem:
            # Validar tamanho (máx 5MB)
            if imagem.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    'O tamanho da imagem não pode exceder 5MB.'
                )
            
            # Validar tipo de arquivo
            tipos_permitidos = ['image/jpeg', 'image/png', 'image/gif']
            if imagem.content_type not in tipos_permitidos:
                raise forms.ValidationError(
                    'Formato de imagem inválido. Use JPG, PNG ou GIF.'
                )
        
        return imagem

