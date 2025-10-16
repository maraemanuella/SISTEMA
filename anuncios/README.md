# App de Anúncios de Carros

## Descrição
Este app gerencia anúncios de venda de carros, permitindo que usuários autenticados criem, visualizem e busquem anúncios de veículos.

## Estrutura

### Models
- **AnuncioCarro**: Modelo principal que armazena todas as informações do anúncio
  - Informações básicas: título, descrição, status
  - Dados do veículo: marca, modelo, ano, km, câmbio, combustível, preço, cor
  - Imagens: imagem principal e imagens adicionais (JSON)
  - Localização: cidade e estado
  - Controle: usuário e data de publicação

### Views
- **ListarAnuncios**: Lista todos os anúncios ativos com paginação, busca e filtros
- **DetalheAnuncio**: Exibe detalhes completos de um anúncio com sugestões relacionadas
- **CriarAnuncio**: Permite criar novos anúncios (requer login)

### Forms
- **AnuncioCarroForm**: Formulário com validações customizadas para criação de anúncios
  - Validação de ano (1900 até ano atual + 1)
  - Validação de preço (maior que zero)
  - Validação de quilometragem (não negativa)
  - Validação de imagem (tamanho máx 5MB, formatos JPG/PNG/GIF)

### Templates
- **listar.html**: Página principal com grid de anúncios
- **detalhe.html**: Página de detalhes com informações completas
- **criar.html**: Formulário de criação de anúncios

## Funcionalidades

### Listagem de Anúncios
- Exibição em grid responsivo (3 colunas em desktop)
- Paginação (12 anúncios por página)
- Busca por texto (título, descrição, marca, modelo, cidade)
- Filtros por: marca, combustível, câmbio, estado
- Ordenação customizável
- Botão para criar novo anúncio

### Detalhes do Anúncio
- Visualização completa das informações
- Imagem principal destacada
- Especificações técnicas organizadas
- Informações de localização
- Dados do anunciante
- Botão de contato via WhatsApp
- Sugestões de anúncios relacionados (mesma marca)

### Criação de Anúncios
- Formulário organizado em seções lógicas
- Preview de imagem em tempo real
- Validações client-side e server-side
- Mensagens de sucesso/erro
- Associação automática com usuário logado
- Redirecionamento para lista após sucesso

## URLs
- `/anuncios/` - Lista de anúncios
- `/anuncios/criar/` - Criar novo anúncio
- `/anuncios/<id>/` - Detalhes do anúncio

## Permissões
- **Visualização**: Todos os usuários (autenticados ou não)
- **Criação**: Apenas usuários autenticados
- **Edição/Exclusão**: Implementação futura

## Melhorias Futuras
- [ ] Edição de anúncios
- [ ] Exclusão de anúncios
- [ ] Upload de múltiplas imagens
- [ ] Sistema de favoritos
- [ ] Compartilhamento em redes sociais
- [ ] Filtros avançados (faixa de preço, ano)
- [ ] Mapa de localização
- [ ] Histórico de visualizações
- [ ] Destaque de anúncios (premium)
