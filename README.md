# Sistema de Gerenciamento de Veículos

Sistema web desenvolvido em Django para gerenciamento de veículos, permitindo o cadastro e listagem de veículos com suas características específicas.

## Sobre o Projeto

Este sistema foi desenvolvido para facilitar o gerenciamento de uma frota de veículos, permitindo o registro detalhado de informações como marca, modelo, ano, cor e tipo de combustível. O projeto utiliza Django como framework backend e Bootstrap para o frontend, garantindo uma interface responsiva e moderna.

## Tecnologias Utilizadas

- **Python 3.12**
- **Django**: Framework web
- **SQLite3**: Banco de dados
- **Bootstrap**: Framework CSS para interface responsiva
- **HTML/CSS/JavaScript**

## Funcionalidades

- Cadastro de veículos com as seguintes informações:
  - Marca (9 opções incluindo AUDI, BMW, CHEVROLET, etc.)
  - Modelo
  - Ano
  - Cor (6 opções)
  - Tipo de Combustível (4 opções)
- Listagem de veículos
- Interface responsiva e amigável
- Sistema de templates reutilizáveis

## Pré-requisitos

- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/maraemanuella/SISTEMA.git
cd SISTEMA
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install django
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor:
```bash
python manage.py runserver
```

O sistema estará disponível em `http://localhost:8000`

## Autores

* **Mara Emanuella** 

## Status do Projeto

O projeto está em desenvolvimento ativo, com novas funcionalidades sendo adicionadas regularmente.

---
