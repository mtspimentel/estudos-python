class Equipamentos:
    def __init__(self, nome, modelo, quantidade):
        self.nome = nome
        self.modelo = modelo
        self.quantidade = quantidade

class Obra:
    def __init__(self):
        self.ferramentas = []

    def adicionar_ferramenta(self, ferramenta):
        self.ferramentas.append(ferramenta)

    def listar_ferramentas(self):
        for ferramenta in self.ferramentas:
            print(f'Nome: {ferramenta.nome} Modelo: {ferramenta.modelo} - {ferramenta.quantidade} unidades')
       

# Criando os equipamentos
chaves = Equipamentos(nome='Chave', modelo='Phillips', quantidade='3')
cimento = Equipamentos(nome='Portland',modelo='CP-III', quantidade='10')
argamassa = Equipamentos(nome='Argamassa colante', modelo='AC-III', quantidade='8')
parafuso = Equipamentos(nome='GN', modelo='25mm', quantidade='1000')
martelete = Equipamentos(nome='Martelete', modelo='10KG', quantidade='2')


# Criar a obra e adicionar as ferramentas nela
obra = Obra()
obra.adicionar_ferramenta(chaves)
obra.adicionar_ferramenta(cimento)
obra.adicionar_ferramenta(argamassa)
obra.adicionar_ferramenta(parafuso)
obra.adicionar_ferramenta(martelete)

# Lista as ferramentas
obra.listar_ferramentas()