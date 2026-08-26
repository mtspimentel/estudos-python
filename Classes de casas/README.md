# Classe Casa em Python

Exercício desenvolvido durante meus estudos de **Python**, praticando conceitos de **Programação Orientada a Objetos (POO)**.

O programa cria objetos a partir de uma classe `Casa`, permitindo armazenar informações como cor, quantidade de quartos e quantidade de banheiros.

## Sobre o projeto

A classe `Casa` possui três características principais:

* Cor da casa;
* Quantidade de quartos;
* Quantidade de banheiros.

Além de armazenar essas informações, o programa possui métodos para exibir os dados e adicionar um novo quarto à casa.

## Conceitos praticados

Neste exercício foram utilizados:

* Classes;
* Objetos;
* Construtor `__init__`;
* `self`;
* Atributos;
* Métodos;
* Parâmetros;
* Alteração de atributos;
* Estruturas de programação orientada a objetos;
* F-strings.

## Estrutura da classe

A classe `Casa` é definida da seguinte forma:

```python
class Casa:

    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
```

O método `__init__` recebe os dados necessários para criar cada objeto.

## Métodos

### `mostrar_cor()`

Exibe a cor da casa:

```python
casa1.mostrar_cor()
```

### `mostrar_quartos()`

Exibe a quantidade de quartos:

```python
casa1.mostrar_quartos()
```

### `mostrar_banheiros()`

Exibe a quantidade de banheiros:

```python
casa1.mostrar_banheiros()
```

### `adicionar_quarto()`

Adiciona um quarto à casa alterando o valor do atributo `quartos`:

```python
self.quartos += 1
```

Por exemplo, uma casa com 5 quartos passa a ter 6:

```text
Esta casa tem 6 quartos
```

## Criando os objetos

O programa cria duas casas diferentes utilizando a mesma classe:

```python
casa1 = Casa('Azul', 5, 3)
casa2 = Casa('Verde', 2, 1)
```

Cada objeto possui seus próprios atributos.

### Casa 1

```text
Cor: Azul
Quartos: 5
Banheiros: 3
```

Depois de adicionar um quarto:

```text
Quartos: 6
```

### Casa 2

```text
Cor: Verde
Quartos: 2
Banheiros: 1
```

Depois de adicionar um quarto:

```text
Quartos: 3
```

## Exemplo de execução

```text
Casa 1:
A cor da casa é Azul
A casa tem 5 quartos
A casa tem 3 banheiros
Esta casa tem 6 quartos

Casa 2:
A cor da casa é Verde
A casa tem 2 quartos
A casa tem 1 banheiros
Esta casa tem 3 quartos
```

## Objetivo

Este exercício faz parte dos meus estudos de **Programação Orientada a Objetos em Python**, praticando a criação de classes, objetos, atributos e métodos.

Através de exercícios simples como este, estou construindo uma base para desenvolver programas e projetos cada vez mais completos.

---

**Tecnologia:** Python 3
**Conceito principal:** Programação Orientada a Objetos
**Nível:** Iniciante
