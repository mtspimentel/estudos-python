class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')

    def mostrar_quartos(self):
        print(f'A casa tem {self.quartos} quartos')

    def mostrar_banheiros(self):
        print(f'A casa tem {self.banheiros} banheiros')

    def adicionar_quarto(self):
        self.quartos += 1
        print(f'Esta casa tem {self.quartos} quartos')


casa1 = Casa('Azul', 5, 3)
casa2 = Casa('Verde', 2, 1)

print('\nCasa 1:')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()

print('\nCasa 2:')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()
