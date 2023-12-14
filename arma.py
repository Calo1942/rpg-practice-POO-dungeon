class Arma():

    def __init__(self):
        self.armas = ["espada", "baculo", "mano"]
        self.atributos = ["fuerza", "inteligencia", "agilidad"]
        self.nombre = str
        self.atributo = str

    def espada(self):
        self.nombre = self.armas[0]
        self.atributo = self.atributos[0]

    def baculo(self):
        self.nombre = self.armas[1]
        self.atributo = self.atributos[1]

    def mano(self):
        self.nombre = self.armas[2]
        self.atributo = self.atributos[2]

    def status(self):
        print(f"nombre arma: {self.nombre}")
        print(f"atributo: {self.atributo}")
    
    def soltar_arma(self):
        self.mano()

    def iniciar(self):
        self.mano()

#arma = Arma()
#
#arma.iniciar()
#arma.status()
#arma.soltar_arma()
#arma.baculo()
#arma.status()
#arma.soltar_arma()
#arma.espada()
#arma.status()