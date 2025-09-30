from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo

class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculo/listar.html'

    def get_queryset(self):
        return Veiculo.objects.all()
    
class CriarVeiculo(LoginRequiredMixin, CreateView):
    model = Veiculo
    template_name = 'veiculo/novo.html'
    fields = ['marca', 'modelo', 'ano', 'cor', 'combustivel']
    success_url = reverse_lazy('listar-veiculos')