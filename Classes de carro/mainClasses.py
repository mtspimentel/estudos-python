class Carro:  # Aqui é criado a classe
    def __init__(self, cor, ano, modelo, marca):  # Definindos os parametros
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.ligado = True
        self.seta = None

    def informacoes(self):  # Criando uma função para mostrar na tela
        print(f'A cor do carro é {self.cor}')
        print(f'O ano do carro é {self.ano}')
        print(f'O modelo do carro é {self.modelo}')
        print(f'A marca do carro é {self.marca}')

    def ligar(self):
        if not self.ligado:
            self.ligado == True
            print('O carro foi ligado')
        else:
            print('O carro já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro já estava desligado')

    def ligar_seta(self, direcao):
        if not self.ligado:
            print('Ligue o carro primeiro :) ')
            return

        self.seta = direcao
        print(f'Seta ligada para {self.seta}')


carro1 = Carro('Azul', 2015, 'Sport', 'BMW')  # Parametros do carro 1
print(f'\nCarro 1: ')
carro1.informacoes()
carro1.desligar()
carro1.ligar_seta('Direita')
