# Cadastro e Situação do Aluno em Python

Exercício desenvolvido durante meus estudos de **Python**, praticando principalmente **dicionários, estruturas condicionais e repetição**.

## Sobre o projeto

O programa solicita o nome e a média de um aluno e, com base na média informada, determina automaticamente sua situação:

* **Aprovado:** média maior ou igual a 7
* **Recuperação:** média entre 5 e menor que 7
* **Reprovado:** média menor que 5

As informações são armazenadas em um **dicionário** e exibidas ao final do programa.

## Exemplo

```text
Nome do aluno: Matheus
A media foi de: 8

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

- nome é igual a Matheus
- media é igual a 8.0
- situação é igual a Aprovado
```

## Conceitos praticados

Neste exercício foram utilizados:

* Dicionários (`dict`)
* Chaves e valores (`keys` e `values`)
* `input()`
* Conversão de tipos com `str()` e `float()`
* Estruturas condicionais `if`, `elif` e `else`
* Operadores de comparação
* Operadores encadeados
* `for`
* `.items()`
* F-strings

## Estrutura do dicionário

O aluno é armazenado da seguinte forma:

```python
aluno = {
    'nome': 'Matheus',
    'media': 8.0,
    'situação': 'Aprovado'
}
```

Depois, o método `.items()` é utilizado para percorrer as chaves e os valores:

```python
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
```

## Objetivo

Este exercício faz parte da minha evolução nos estudos de Python, buscando entender melhor como trabalhar com **estruturas de dados e lógica de programação**.

## Próximas melhorias

* [ ] Validar se a média está entre 0 e 10
* [ ] Cadastrar vários alunos
* [ ] Criar funções para organizar o código
* [ ] Calcular a média de várias notas
* [ ] Armazenar os alunos em uma lista
* [ ] Criar um sistema de consulta de alunos

---

**Tecnologia utilizada:** Python 3
