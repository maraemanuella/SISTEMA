"""
Views para o app de anúncios de carros.
Gerencia listagem, detalhes e criação de anúncios.
"""
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from anuncios.models import AnuncioCarro
from anuncios.forms import AnuncioCarroForm


class ListarAnuncios(ListView):
    """
    View para listar todos os anúncios ativos com filtros e paginação.
    Permite busca por texto, filtros por marca/combustível/câmbio/estado
    e ordenação customizada.
    """
    
    model = AnuncioCarro
    context_object_name = 'anuncios'
    template_name = 'anuncios/listar.html'
    paginate_by = 12

    def get_queryset(self):
        """Retorna queryset filtrado e ordenado"""
        if not hasattr(self, '_cached_queryset'):
            queryset = AnuncioCarro.objects.filter(status='ativo')
            queryset = self._aplicar_busca(queryset)
            queryset = self._aplicar_filtros(queryset)
            queryset = self._aplicar_ordenacao(queryset)
            self._cached_queryset = queryset
        return self._cached_queryset
    
    def _aplicar_busca(self, queryset):
        """Aplica busca por texto em múltiplos campos"""
        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) |
                Q(descricao__icontains=query) |
                Q(marca__icontains=query) |
                Q(modelo__icontains=query) |
                Q(cidade__icontains=query)
            )
        return queryset
    
    def _aplicar_filtros(self, queryset):
        """Aplica filtros específicos de marca, combustível, câmbio e estado"""
        filtros = {
            'marca': self.request.GET.get('marca'),
            'combustivel': self.request.GET.get('combustivel'),
            'cambio': self.request.GET.get('cambio'),
            'estado': self.request.GET.get('estado'),
        }
        
        for campo, valor in filtros.items():
            if valor:
                queryset = queryset.filter(**{campo: valor})
        
        return queryset
    
    def _aplicar_ordenacao(self, queryset):
        """Aplica ordenação ao queryset"""
        ordem = self.request.GET.get('ordem', '-data_publicacao')
        return queryset.order_by(ordem)
    
    def get_context_data(self, **kwargs):
        """Adiciona dados extras ao contexto para filtros e estatísticas"""
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context.update({
            'query': self.request.GET.get('q', ''),
            'total_anuncios': queryset.count(),
            'filtro_marca': self.request.GET.get('marca', ''),
            'filtro_combustivel': self.request.GET.get('combustivel', ''),
            'filtro_cambio': self.request.GET.get('cambio', ''),
            'filtro_estado': self.request.GET.get('estado', ''),
            'ordem': self.request.GET.get('ordem', '-data_publicacao'),
        })
        return context


class DetalheAnuncio(DetailView):
    """
    View para exibir detalhes completos de um anúncio específico.
    Inclui anúncios relacionados da mesma marca.
    """
    
    model = AnuncioCarro
    context_object_name = 'anuncio'
    template_name = 'anuncios/detalhe.html'
    
    def get_context_data(self, **kwargs):
        """Adiciona anúncios relacionados ao contexto"""
        context = super().get_context_data(**kwargs)
        context['anuncios_relacionados'] = self._get_anuncios_relacionados()
        return context
    
    def _get_anuncios_relacionados(self):
        """Retorna até 4 anúncios relacionados da mesma marca"""
        anuncio = self.get_object()
        return AnuncioCarro.objects.filter(
            marca=anuncio.marca,
            status='ativo'
        ).exclude(id=anuncio.id)[:4]


class CriarAnuncio(LoginRequiredMixin, CreateView):
    """
    View para criar um novo anúncio de carro.
    Requer autenticação e associa automaticamente o usuário logado.
    """
    
    model = AnuncioCarro
    form_class = AnuncioCarroForm
    template_name = 'anuncios/criar.html'
    success_url = reverse_lazy('listar-anuncios')
    login_url = 'login'
    
    def form_valid(self, form):
        """
        Associa o usuário logado ao anúncio e define status como ativo.
        Exibe mensagem de sucesso após criação.
        """
        form.instance.usuario = self.request.user
        form.instance.status = 'ativo'
        messages.success(
            self.request, 
            f'Anúncio "{form.instance.titulo}" criado com sucesso!'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Exibe mensagem de erro caso o formulário seja inválido"""
        messages.error(
            self.request,
            'Erro ao criar anúncio. Verifique os campos e tente novamente.'
        )
        return super().form_invalid(form)

