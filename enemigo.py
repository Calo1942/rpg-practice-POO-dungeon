
class Enemigo:
    
    def __init__(self):
        self.enemigos = ["orco", "elfo", "humano"]
        self.atributos = ["fuerza", "inteligencia", "agilidad"]
        self.nombre = str
        self.atributo = str

    def orco(self):
        self.nombre = self.enemigos[0]
        self.atributo = self.atributos[0]
    
    def elfo(self):
        self.nombre = self.enemigos[1]
        self.atributo = self.atributos[1]
    
    def humano(self):
        self.nombre = self.enemigos[2]
        self.atributo = self.atributos[2]

    def select_enemy(self):
        
        import random
        enemy_num = random.randint(0, 2)

        if enemy_num == 0:
            self.orco()
        elif enemy_num == 1:
            self.elfo()
        elif enemy_num == 2:
            self.humano()

    def status(self):
        print(f"enemigo: {self.nombre}")
        print(f"atributo: {self.atributo}")

    def iniciar(self):
        self.select_enemy()
