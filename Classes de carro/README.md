# Classe Carro em Python

Exercício desenvolvido durante meus estudos de **Python**, com foco nos primeiros conceitos de **Programação Orientada a Objetos (POO)**.

O programa cria uma classe `Carro` com informações e comportamentos básicos de um veículo, como ligar, desligar e acionar a seta.

## Sobre o projeto

A classe `Carro` recebe algumas características do veículo:

* Cor;
* Ano;
* Modelo;
* Marca.

Além dessas informações, o objeto possui estados que podem ser alterados durante a execução:

* Carro ligado ou desligado;
* Direção da seta.

## Conceitos praticados

Neste exercício foram utilizados:

* Classes;
* Objetos;
* Construtor `__init__`;
* `self`;
* Atributos;
* Métodos;
* Parâmetros;
* Condicionais `if/else`;
* Retorno com `return`;
* F-strings;
* Alteração de estado de um objeto.

## Estrutura da classe

A classe `Carro` é criada da seguinte forma:

```python
class Carro:
```

O método `__init__` é utilizado para definir os atributos que cada objeto terá:

```python
def __init__(self, cor, ano, modelo, marca):
    self.cor = cor
    self.ano = ano
    self.modelo = modelo
    self.marca = marca
    self.ligado = True
    self.seta = None
```

Dessa forma, cada carro criado pode possuir suas próprias informações.

## Métodos

### `informacoes()`

Exibe as informações do carro:

```python
carro1.informacoes()
```

### `ligar()`

Verifica se o carro está desligado e, caso esteja, realiza a alteração do seu estado.

### `desligar()`

Verifica se o carro está ligado e altera seu estado para desligado.

### `ligar_seta()`

Recebe uma direção e aciona a seta do carro.

O método também verifica se o carro está ligado antes de permitir o acionamento:

```python
carro1.ligar_seta('Direita')
```

## Criando um objeto

Um objeto da classe `Carro` é criado passando os valores definidos no construtor:

```python
carro1 = Carro('Azul', 2015, 'Sport', 'BMW')
```

Nesse caso, o objeto possui:

```text
Cor: Azul
Ano: 2015
Modelo: Sport
Marca: BMW
```

## Exemplo de execução

```text
Carro 1:

A cor do carro é Azul
O ano do carro é 2015
O modelo do carro é Sport
A marca do carro é BMW

O carro foi desligado
Ligue o carro primeiro :)
```

O último resultado acontece porque, após desligar o carro, o programa tenta acionar a seta. Como o veículo está desligado, o método impede a operação.

## Objetivo

Este exercício faz parte da minha evolução nos estudos de Python e representa um dos primeiros contatos com **Programação Orientada a Objetos**.

O objetivo é entender como criar classes, definir atributos, criar métodos e controlar o estado dos objetos.

## Próximos passos

A ideia é continuar evoluindo o projeto, adicionando novos comportamentos ao carro e aprofundando os estudos de **POO em Python**.

---

**Tecnologia:** Python 3
**Conceito principal:** Programação Orientada a Objetos
**Nível:** Iniciante
