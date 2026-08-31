# *** Herança multipla e Herança multinível *** #
# Classe geral
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

# Classes Pai
class Predador(Animal):
    def __init__ (self, nome, idade, velocidade, **kwargs):
        super().__init__(nome, idade, **kwargs)
        self.velocidade = velocidade

    def cacar(self):
        print(f'{self.nome} está caçando')

    def atacar(self):
        print(f'{self.nome} atacou a presa!')


class Presa(Animal):
    def __init__(self, nome, idade, velocidade_fuga, **kwargs):
        super().__init__(nome, idade, **kwargs)
        self.velocidade_fuga = velocidade_fuga

    def fugir(self):
        print(f'O {self.nome} está fugindo!')

    def esconder(self):
        print(f'{self.nome} está procurando um lugar para se esconder')

# Classes filho
class Coelho(Presa):
    def emitir_som(self):
        print(f'{self.nome} fez: Squeak!')

class Tigre(Predador):
    def emitir_som(self):
        print(f'{self.nome} rugiu: Grrrrrr! ')

class Golfinho(Predador, Presa):
    def __init__(self, nome, idade, velocidade, velocidade_fuga):
        super().__init__(
            nome=nome,
            idade=idade,
            velocidade=velocidade,
            velocidade_fuga=velocidade_fuga
              )


    def emitir_som(self):
        print(f'{self.nome} fez: Click click!')

    def nadar(self):
        print(f'{self.nome} está nadando')

coelho1 = Coelho('tico', 2, 30)
tigre1 = Tigre('simba', 5, 80)
golfinho1 = Golfinho('marley', 4, 40, 30)

print('\n --- Coelho ---')
coelho1.apresentar()
coelho1.fugir()
coelho1.esconder()
coelho1.emitir_som()

print('\n --- Tigre ---')
tigre1.apresentar()
tigre1.cacar()
tigre1.atacar()
tigre1.emitir_som()

print('\n --- Golfinho ---')
golfinho1.apresentar()
golfinho1.cacar()
golfinho1.fugir()
golfinho1.nadar()
golfinho1.emitir_som()