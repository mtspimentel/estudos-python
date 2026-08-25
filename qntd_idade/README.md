# Cadastro de Pessoas em Python

Exercício desenvolvido durante meus estudos de **Python**, com foco em estruturas de repetição, condicionais, validação de dados e interação com o usuário.

## Sobre o projeto

O programa permite cadastrar várias pessoas informando:

* Idade;
* Sexo.

Ao final dos cadastros, o programa apresenta:

* Quantidade de pessoas com mais de 18 anos;
* Quantidade de homens cadastrados;
* Quantidade de mulheres com menos de 20 anos.

O usuário também pode escolher se deseja continuar cadastrando ou encerrar o programa.

## Conceitos praticados

Neste exercício foram utilizados:

* `while True`;
* Estruturas condicionais `if`;
* Validação de entrada;
* `break`;
* Variáveis contadoras;
* `input()`;
* Conversão de dados com `int()`;
* Métodos `.upper()` e `.strip()`;
* Operadores de comparação;
* Operadores lógicos;
* F-strings.

## Como funciona

O programa inicia solicitando a idade da pessoa:

```python
idade = int(input('Idade: '))
```

Depois verifica se a pessoa possui mais de 18 anos:

```python
if idade > 18:
    maior18 += 1
```

Em seguida, solicita o sexo e valida a entrada para aceitar apenas `M` ou `F`:

```python
sexo = ' '

while sexo not in 'MF':
    sexo = str(input('Sexo: [M/F]:')).upper().strip()[0]
```

O programa também conta os homens cadastrados e as mulheres com menos de 20 anos.

Por fim, pergunta se o usuário deseja realizar outro cadastro:

```python
continua = ' '

while continua not in 'SN':
    continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]

if continua == 'N':
    break
```

Quando o usuário escolhe `N`, o programa encerra o cadastro e apresenta os resultados.

## Objetivo

Este exercício faz parte da minha jornada de aprendizado em Python e tem como objetivo praticar **lógica de programação e manipulação de dados através de entradas do usuário**.

A ideia é evoluir esses exercícios gradualmente, aplicando novos conceitos e transformando o aprendizado em projetos cada vez mais completos.

---

**Tecnologia:** Python 3
**Foco:** Lógica de programação e estruturas de repetição
