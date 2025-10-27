from django.urls import path

from sistema.api import ObtainAuthTokenView, VehicleListView


app_name = 'api'

urlpatterns = [
    path('listar/', VehicleListView.as_view(), name='listar-veiculos'),
    path('token-auth/', ObtainAuthTokenView.as_view(), name='token-auth'),
]
