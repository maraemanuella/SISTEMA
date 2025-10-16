from django import template
from sistema.constantes import OPCOES_MARCAS, OPCOES_COMBUSTIVEL, OPCOES_CAMBIO, OPCOES_ORDENACAO

register = template.Library()


@register.inclusion_tag('anuncios/components/card_anuncio.html')
def card_anuncio(anuncio):
    """Renderiza um card de anúncio"""
    return {'anuncio': anuncio}


@register.inclusion_tag('anuncios/components/filtros.html')
def filtros_anuncios(filtro_marca='', filtro_combustivel='', filtro_cambio='', ordem='-data_publicacao'):
    """Renderiza os filtros de busca"""
    return {
        'marcas': OPCOES_MARCAS,
        'combustiveis': OPCOES_COMBUSTIVEL,
        'cambios': OPCOES_CAMBIO,
        'ordenacoes': OPCOES_ORDENACAO,
        'filtro_marca': filtro_marca,
        'filtro_combustivel': filtro_combustivel,
        'filtro_cambio': filtro_cambio,
        'ordem': ordem,
    }


@register.inclusion_tag('anuncios/components/card_veiculo_placeholder.html')
def placeholder_veiculo():
    """Renderiza placeholder para imagem de veículo"""
    return {}


@register.inclusion_tag('anuncios/components/paginacao.html', takes_context=True)
def paginacao(context):
    """Renderiza a paginação com query string preservada"""
    request = context['request']
    
    # Constrói query string mantendo os parâmetros atuais
    params = []
    for key, value in request.GET.items():
        if key != 'page' and value:
            params.append(f'&{key}={value}')
    
    query_string = ''.join(params)
    
    return {
        'is_paginated': context.get('is_paginated', False),
        'page_obj': context.get('page_obj'),
        'query_string': query_string,
    }
