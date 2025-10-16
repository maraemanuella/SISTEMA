from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib import messages
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from veiculo.const import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEL

class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculo/listar.html'

    def get_queryset(self):
        queryset = Veiculo.objects.all()
        query = self.request.GET.get('q')
        
        if query:
            query = query.strip()
            
            # Criar Q objects para busca
            q_objects = Q()
            
            # Busca por modelo (case insensitive)
            q_objects |= Q(modelo__icontains=query)
            
            # Busca por ano (se for um número)
            if query.isdigit():
                q_objects |= Q(ano=int(query))
            
            # Busca por marca (comparando com os nomes das marcas)
            for marca_value, marca_nome in OPCOES_MARCAS:
                if query.lower() in marca_nome.lower():
                    q_objects |= Q(marca=marca_value)
            
            # Busca por cor
            for cor_value, cor_nome in OPCOES_CORES:
                if query.lower() in cor_nome.lower():
                    q_objects |= Q(cor=cor_value)
            
            # Busca por combustível
            for combustivel_value, combustivel_nome in OPCOES_COMBUSTIVEL:
                if query.lower() in combustivel_nome.lower():
                    q_objects |= Q(combustivel=combustivel_value)
            
            queryset = queryset.filter(q_objects)
        
        return queryset.order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
    
class CriarVeiculo(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')
    
    def form_valid(self, form):
        """
        Método chamado quando o formulário é válido.
        Aqui podemos adicionar lógica adicional se necessário.
        """
        messages.success(self.request, 'Veículo cadastrado com sucesso!')
        response = super().form_valid(form)
        return response
    
    
class EditarVeiculo(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')
    context_object_name = 'veiculo'
    
    def form_valid(self, form):
        """
        Método chamado quando o formulário é válido.
        Aqui podemos adicionar lógica adicional se necessário.
        """
        messages.success(self.request, 'Veículo atualizado com sucesso!')
        response = super().form_valid(form)
        return response
    
class DeletarVeiculo(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo/confirmar_exclusao.html'
    success_url = reverse_lazy('listar-veiculos')
    context_object_name = 'veiculo'
    
    def delete(self, request, *args, **kwargs):
        """
        Sobrescreve o método delete para adicionar mensagem de sucesso.
        """
        veiculo = self.get_object()
        messages.success(request, f'Veículo {veiculo.get_marca_display()} {veiculo.modelo} foi excluído com sucesso!')
        return super().delete(request, *args, **kwargs)
    
class FotoVeiculo(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = 'veiculo/foto.html'
    context_object_name = 'veiculos'
    
    def get_queryset(self):
        arquivo = self.kwargs.get('arquivo')
        if arquivo:
            return Veiculo.objects.filter(foto__icontains=arquivo)
        else:
            raise Http404("Arquivo não especificado")