from django.contrib import admin
from django.utils.html import format_html
from anuncios.models import AnuncioCarro


@admin.register(AnuncioCarro)
class AnuncioCarroAdmin(admin.ModelAdmin):
    """Configuração do admin para AnuncioCarro"""
    
    list_display = [
        'titulo', 'marca', 'modelo', 'ano', 
        'preco_formatado', 'status', 'data_publicacao'
    ]
    list_filter = ['status', 'marca', 'combustivel', 'cambio', 'estado', 'data_publicacao']
    search_fields = ['titulo', 'descricao', 'marca', 'modelo', 'cidade']
    list_editable = ['status']
    ordering = ['-data_publicacao']
    date_hierarchy = 'data_publicacao'
    list_per_page = 25
    
    fieldsets = (
        ('Informações do Anúncio', {
            'fields': ('titulo', 'descricao', 'status')
        }),
        ('Informações do Veículo', {
            'fields': ('marca', 'modelo', 'ano', 'km', 'cambio', 'combustivel', 'preco', 'cor')
        }),
        ('Imagens', {
            'fields': ('imagem_principal', 'imagens_adicionais')
        }),
        ('Localização', {
            'fields': ('cidade', 'estado')
        }),
        ('Controle', {
            'fields': ('usuario', 'data_publicacao'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['data_publicacao']
    
    @admin.display(description='Preço', ordering='preco')
    def preco_formatado(self, obj):
        """Exibe o preço formatado"""
        return obj.get_preco_formatado()
    
    @admin.display(description='Status', ordering='status')
    def status_badge(self, obj):
        """Exibe o status com badge colorido"""
        cores = {
            'ativo': 'success',
            'inativo': 'secondary',
            'vendido': 'warning'
        }
        cor = cores.get(obj.status, 'secondary')
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            cor,
            obj.get_status_display()
        )
    
    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',)
        }
