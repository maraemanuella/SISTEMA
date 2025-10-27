"""
URLs para o app de anúncios de carros.
Define as rotas para listagem, criação e visualização de anúncios.
"""
from django.urls import path

from anuncios import views


app_name = 'anuncios'


urlpatterns = [
    # Listagem de anúncios
    path('', views.ListarAnuncios.as_view(), name='listar-anuncios'),
    
    # Criar novo anúncio
    path('criar/', views.CriarAnuncio.as_view(), name='criar-anuncio'),
    
    # Detalhes do anúncio (deve ficar por último para não conflitar)
    path('<int:pk>/', views.DetalheAnuncio.as_view(), name='detalhe-anuncio'),
]
