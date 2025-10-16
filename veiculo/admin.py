from django.contrib import admin
from veiculo.models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'cor', 'combustivel', 'foto')
    list_filter = ('marca', 'ano', 'cor', 'combustivel')
    search_fields = ('marca', 'modelo', 'ano')
    ordering = ('-ano', 'marca', 'modelo')
