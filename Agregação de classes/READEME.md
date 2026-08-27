# Controle de Equipamentos de Obra em Python

Projeto desenvolvido durante meus estudos de **Python e Programação Orientada a Objetos (POO)**.

O exercício simula um controle simples de equipamentos e materiais utilizados em uma obra, permitindo cadastrar itens, adicioná-los a uma obra e listar todos os equipamentos cadastrados.

## Sobre o projeto

O programa utiliza duas classes:

### `Equipamentos`

Representa um equipamento ou material utilizado na obra.

Cada equipamento possui:

* Nome;
* Modelo;
* Quantidade.

### `Obra`

Representa uma obra que possui uma lista de ferramentas e materiais cadastrados.

A classe permite:

* Adicionar equipamentos à obra;
* Listar os equipamentos cadastrados.

## Conceitos praticados

Neste exercício foram utilizados:

* Programação Orientada a Objetos (POO);
* Classes;
* Objetos;
* Construtor `__init__`;
* Atributos;
* Métodos;
* Listas;
* `append()`;
* Laço `for`;
* Relacionamento entre classes;
* F-strings;
* Parâmetros nomeados.

## Estrutura do projeto

O projeto possui duas classes principais:

```python
class Equipamentos:

    def __init__(self, nome, modelo, quantidade):
        self.nome = nome
        self.modelo = modelo
        self.quantidade = quantidade
```

A classe `Obra` possui uma lista onde os equipamentos são armazenados:

```python
class Obra:

    def __init__(self):
        self.ferramentas = []
```

Para adicionar um equipamento à lista, é utilizado o método:

```python
def adicionar_ferramenta(self, ferramenta):
    self.ferramentas.append(ferramenta)
```

E para visualizar os equipamentos cadastrados:

```python
def listar_ferramentas(self):

    for ferramenta in self.ferramentas:
        print(
            f'Nome: {ferramenta.nome} '
            f'Modelo: {ferramenta.modelo} '
            f'- {ferramenta.quantidade} unidades'
        )
```

## Equipamentos cadastrados

O programa cria alguns exemplos de materiais e ferramentas:

| Nome              | Modelo   | Quantidade |
| ----------------- | -------- | ---------: |
| Chave             | Phillips |          3 |
| Portland          | CP-III   |         10 |
| Argamassa colante | AC-III   |          8 |
| GN                | 25mm     |       1000 |
| Martelete         | 10KG     |          2 |

## Exemplo de execução

```text
Nome: Chave Modelo: Phillips - 3 unidades
Nome: Portland Modelo: CP-III - 10 unidades
Nome: Argamassa colante Modelo: AC-III - 8 unidades
Nome: GN Modelo: 25mm - 1000 unidades
Nome: Martelete Modelo: 10KG - 2 unidades
```

## Como executar

1. Tenha o **Python 3** instalado.
2. Clone este repositório.
3. Execute o arquivo `.py` pelo terminal ou pela sua IDE.

Exemplo:

```bash
python equipamentos.py
```

## Objetivo

Este projeto faz parte da minha evolução nos estudos de **Python**, principalmente na área de **Programação Orientada a Objetos**.

Também representa uma tentativa de aplicar os conhecimentos de programação em um contexto que faz parte da minha experiência profissional: **obras e construção civil**.

## Próximos passos

Algumas melhorias que podem ser implementadas futuramente:

* Adicionar equipamentos;
* Remover equipamentos;
* Alterar quantidade;
* Pesquisar equipamentos;
* Controlar entrada e saída de materiais;
* Criar um sistema de estoque;
* Utilizar banco de dados;
* Criar uma interface para o sistema.

---

**Tecnologia:** Python 3
**Conceito principal:** Programação Orientada a Objetos
**Nível:** Iniciante
