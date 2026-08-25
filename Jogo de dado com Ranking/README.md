# Jogo de Dados e Ranking em Python

Exercício desenvolvido durante meus estudos de **Python**, com o objetivo de praticar dicionários, funções de módulos, ordenação de dados e estruturas de repetição.

## Sobre o projeto

O programa simula um jogo de dados entre quatro jogadores.

Cada jogador recebe um número aleatório entre **1 e 6** e, após os sorteios, os jogadores são organizados em um ranking do maior para o menor resultado.

## Funcionamento

1. O programa sorteia um número de 1 a 6 para cada jogador.
2. Os resultados são armazenados em um dicionário.
3. Os valores sorteados são exibidos na tela.
4. Os jogadores são ordenados de acordo com o resultado.
5. O programa apresenta o ranking final.

## Exemplo

```text
Valores sorteados:
Jogador1 tirou 5 no dado.
Jogador2 tirou 2 no dado.
Jogador3 tirou 6 no dado.
Jogador4 tirou 4 no dado.

==============================

  == RANKING DOS JOGADORES ==

   1º lugar: Jogador3 com 6
   2º lugar: Jogador1 com 5
   3º lugar: Jogador4 com 4
   4º lugar: Jogador2 com 2
```

## Conceitos praticados

Neste exercício foram utilizados:

* `random.randint()`
* `time.sleep()`
* `operator.itemgetter()`
* Dicionários
* `.items()`
* `sorted()`
* `enumerate()`
* `for`
* `key`
* `reverse`
* F-strings

## Destaque do código

A parte responsável por organizar o ranking é:

```python
ranking = sorted(
    jogo.items(),
    key=itemgetter(1),
    reverse=True
)
```

O `itemgetter(1)` indica que a ordenação deve considerar o **valor do dicionário**, que nesse caso é o número sorteado no dado.

O `reverse=True` faz com que a ordem seja **decrescente**, colocando primeiro quem tirou o maior número.

## Estrutura dos dados

Os resultados são armazenados em um dicionário:

```python
jogo = {
    'Jogador1': 5,
    'Jogador2': 2,
    'Jogador3': 6,
    'Jogador4': 4
}
```

Depois, `.items()` transforma os dados em pares de chave e valor para que possam ser ordenados.

## Objetivo

Este exercício faz parte da minha evolução nos estudos de Python, praticando cada vez mais o uso de **estruturas de dados, funções e organização de informações**.

## Próximas melhorias

* [ ] Permitir que o usuário escolha a quantidade de jogadores
* [ ] Permitir várias rodadas
* [ ] Criar um sistema de pontuação
* [ ] Identificar automaticamente o vencedor
* [ ] Tratar empates
* [ ] Criar funções para organizar o código

---

**Tecnologia utilizada:** Python 3
