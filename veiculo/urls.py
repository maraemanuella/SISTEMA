from django.urls import path

from veiculo.views import (
    CriarVeiculo,
    DeletarVeiculo,
    EditarVeiculo,
    FotoVeiculo,
    ListarVeiculos,
)


app_name = 'veiculo'


urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculo.as_view(), name='criar-veiculo'),
    path('editar/<int:pk>/', EditarVeiculo.as_view(), name='editar-veiculo'),
    path('deletar/<int:pk>/', DeletarVeiculo.as_view(), name='deletar-veiculo'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='exibir-foto'),
]
