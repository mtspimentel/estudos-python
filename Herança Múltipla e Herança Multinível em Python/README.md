# 🐾 Herança Múltipla e Herança Multinível em Python

Projeto desenvolvido durante meus estudos de **Python e Programação Orientada a Objetos (POO)**, com foco na utilização de **herança múltipla, herança multinível e sobrescrita de métodos**.

O projeto utiliza animais como exemplo para demonstrar como diferentes classes podem herdar características e comportamentos de outras classes.

## 📚 Sobre o projeto

A estrutura do programa possui uma classe geral `Animal` e classes derivadas que representam diferentes tipos de animais.

A hierarquia foi construída da seguinte forma:

```text
Animal
├── Predador
│   └── Tigre
│
├── Presa
│   └── Coelho
│
└── Golfinho
    ├── Predador
    └── Presa
```

O `Golfinho` é utilizado para demonstrar **herança múltipla**, pois herda características tanto de `Predador` quanto de `Presa`.

Já `Tigre` e `Coelho` demonstram **herança multinível**, pois suas características são herdadas através de uma cadeia de classes.

## 🧠 Conceitos praticados

Neste projeto foram praticados:

* Programação Orientada a Objetos;
* Herança;
* Herança múltipla;
* Herança multinível;
* Classes pai e classes filho;
* `super()`;
* `**kwargs`;
* Sobrescrita de métodos;
* Polimorfismo;
* MRO (Method Resolution Order);
* Construtor `__init__`;
* Atributos e métodos.

## 🏛️ Classe `Animal`

A classe `Animal` funciona como a classe base do projeto.

Ela possui atributos comuns a todos os animais:

* `nome`;
* `idade`.

Também possui métodos que podem ser utilizados pelas classes derivadas:

```python
class Animal:

    def __init__(self, nome, idade, **kwargs):
        super().__init__(**kwargs)
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')

    def emitir_som(self):
        print('O animal emitiu um som')
```

## 🐅 Classe `Predador`

A classe `Predador` herda de `Animal`.

Além dos atributos herdados, possui:

* `velocidade`.

Também adiciona comportamentos específicos:

* `cacar()`;
* `atacar()`.

```python
class Predador(Animal):
```

## 🐇 Classe `Presa`

A classe `Presa` também herda de `Animal`.

Possui o atributo:

* `velocidade_fuga`.

E adiciona os métodos:

* `fugir()`;
* `esconder()`.

```python
class Presa(Animal):
```

## 🐰 Classe `Coelho`

O `Coelho` herda de `Presa`:

```python
class Coelho(Presa):
```

Com isso, ele possui acesso aos comportamentos de `Presa` e `Animal`.

O método `emitir_som()` é sobrescrito para apresentar um comportamento específico:

```python
def emitir_som(self):
    print(f'{self.nome} fez: Squeak!')
```

## 🐯 Classe `Tigre`

O `Tigre` herda de `Predador`:

```python
class Tigre(Predador):
```

Dessa forma, pode utilizar métodos como:

```python
tigre1.cacar()
tigre1.atacar()
```

E também sobrescreve o método `emitir_som()`:

```python
def emitir_som(self):
    print(f'{self.nome} rugiu: Grrrrrr!')
```

## 🐬 Herança múltipla com `Golfinho`

O principal exemplo do projeto é a classe `Golfinho`:

```python
class Golfinho(Predador, Presa):
```

Nesse caso, o `Golfinho` herda de **duas classes diferentes**:

* `Predador`;
* `Presa`.

Por isso, ele pode utilizar comportamentos das duas classes:

```python
golfinho1.cacar()
golfinho1.fugir()
```

Além disso, possui seu próprio comportamento:

```python
golfinho1.nadar()
```

E sobrescreve `emitir_som()`:

```python
def emitir_som(self):
    print(f'{self.nome} fez: Click click!')
```

## 🔄 Uso do `super()`

O projeto também utiliza `super()` para permitir que os construtores das classes sejam chamados seguindo a cadeia de herança.

Exemplo:

```python
super().__init__(
    nome=nome,
    idade=idade,
    velocidade=velocidade,
    velocidade_fuga=velocidade_fuga
)
```

O uso de `**kwargs` permite encaminhar argumentos entre as diferentes classes da hierarquia.

Isso é especialmente importante no exemplo de **herança múltipla**, onde o Python utiliza a **MRO (Method Resolution Order)** para determinar a ordem em que os métodos são encontrados.

## ▶️ Exemplo de execução

### Coelho

```text
--- Coelho ---
Nome: tico
Idade: 2 anos
O tico está fugindo!
tico está procurando um lugar para se esconder
tico fez: Squeak!
```

### Tigre

```text
--- Tigre ---
Nome: simba
Idade: 5 anos
simba está caçando
simba atacou a presa!
simba rugiu: Grrrrrr!
```

### Golfinho

```text
--- Golfinho ---
Nome: marley
Idade: 4 anos
marley está caçando
O marley está fugindo!
marley está nadando
marley fez: Click click!
```

## 🎯 Objetivo

O objetivo deste exercício é aprofundar meus conhecimentos em **Programação Orientada a Objetos**, saindo dos conceitos básicos de classes e objetos e avançando para estruturas de herança mais complexas.

Este projeto representa mais uma etapa da minha evolução nos estudos de **Python e desenvolvimento de software**.

---

**Tecnologia:** Python 3
**Conceito principal:** Programação Orientada a Objetos
**Tópicos:** Herança múltipla, herança multinível, `super()` e polimorfismo
