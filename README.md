# Fifinha - Django FIFA Fake

## Descrição

O projeto **Fifinha** é uma aplicação web desenvolvida com Django que simula um sistema de cadastro e exibição de jogadores de futebol, inspirado no modelo de atributos do FIFA.

A aplicação permite cadastrar jogadores com seus atributos e visualizá-los em uma interface web.

---

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- HTML e CSS

---

## Arquitetura

O projeto segue o padrão **MTV (Model, Template, View)** do Django:

- **Model**: Define a estrutura dos dados (Jogador)
- **View**: Controla a lógica e envio de dados
- **Template**: Renderiza os dados no navegador

---

## Funcionalidades

- Cadastro de jogadores via admin
- Visualização de jogadores no navegador
- Atributos(não precisa ser todos):
  - Nome
  - Time
  - Posição
  - Overall
  - Pace
  - Shooting
  - Passing
  - Dribbling
  - Defense
  - Physical

---

## Estrutura do Projeto(meu exemplo)

```
DJANGO_FIFA_FAKE/
├── manage.py
├── DJANGO_FIFA_FAKE/
│   ├── settings.py
│   ├── urls.py
│
├── jogadores/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── templates/
│       └── jogadores/
│           └── lista.html
```

---

## Como Executar

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

---

## Objetivo

Projeto desenvolvido para prática de:

- Django básico
- CRUD com models
- Uso do admin
- Templates e rotas
Pensado paenas para testes

---

## Melhorias Futuras

- Layout estilo cards FIFA
- Imagens dos jogadores
- Filtros e busca

---

## Autor Tiago, aluno SENAICTTI 

Projeto acadêmico para aprendizado de desenvolvimento web com Django.
Porem não me garanto muito :,D

---

## Exemplos para incluir nos dados dos jogadores

Exemplo 1 (jogador atacante)
Nome: Neymar Jr
Time: Al-Hilal
Posição: LW
Overall: 89
Pace: 87
Shooting: 85
Passing: 86
Dribbling: 92
Defense: 37
Physical: 60

Exemplo 2 (jogador completo)
Nome: Kevin De Bruyne
Time: Manchester City
Posição: CM
Overall: 91
Pace: 74
Shooting: 86
Passing: 93
Dribbling: 88
Defense: 64
Physical: 78

Exemplo 3 (defensor)
Nome: Virgil van Dijk
Time: Liverpool
Posição: CB
Overall: 90
Pace: 78
Shooting: 60
Passing: 71
Dribbling: 72
Defense: 91
Physical: 86

Exemplo 4 (goleiro adaptado)
Nome: Alisson Becker
Time: Liverpool
Posição: GK
Overall: 89
Pace: 50
Shooting: 20
Passing: 70
Dribbling: 60
Defense: 85
Physical: 80


