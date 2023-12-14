import arma
import enemigo

class Personaje():

    def __init__(self) -> None:
        self.nombre = str
        self.arma = arma.Arma()
        self.enemigo = enemigo.Enemigo()

    def status(self):
        print(f"Tu arma es: {self.arma.nombre}")
        print(f"El atributo de tu arma es: {self.arma.atributo}")
        print(f"Tu enemigo es de atributo: {self.enemigo.atributo}")
        self.bucle()

    def select_arma(self):
        print("1 espada, 2 baculo, 3 mano: ")
        choice = input("Seleciona un arma: ")
        if choice == "1":
            self.arma.espada()
            self.bucle()
        elif choice == "2":
            self.arma.baculo()
            self.bucle()
        elif choice == "3":
            self.arma.mano()
            self.bucle()
        else:
            print("Comando inválido, intenta nuevamente")
            self.select_arma()

    def pelear(self):
        if self.enemigo.atributo == self.arma.atributo:
            
            import random
            probabilidad = random.randint(0,1)
            
            if probabilidad == False:
                self.perdiste()
            else:
                self.ganaste()

        elif self.enemigo.atributo == "fuerza" and self.arma.atributo == "inteligencia":
            self.ganaste()
        elif self.enemigo.atributo == "inteligencia" and self.arma.atributo == "agilidad":
            self.ganaste()
        elif self.enemigo.atributo == "agilidad" and self.arma.atributo == "fuerza":
            self.ganaste()
        else:
            self.perdiste()

    def ganaste(self):
        print("¡Has Ganado esta batalla!")
        self.volver_jugar()

    def perdiste(self):
        print("¡Has perdido esta vez!")
        self.volver_jugar()

    def salir(self):
        print("Adiós")

    def volver_jugar(self):
        choice = input("¿Quieres volver a jugar? y/n: ")
        if choice in ["y", "yes", "si", "s", "Y", "YES", "SI", "S"]:
            self.enemigo.select_enemy()
            self.bucle()
        elif choice in ["n", "no", "N", "NO"]:
            self.salir()
        else:
            print("comando inválido, prueba otra vez")
            self.volver_jugar()

    def bucle(self):
        print(f"te enfrentas a un {self.enemigo.nombre}")
        print("1 pelear, 2 cambiar arma, 3 estatus, 4 salir")
        choice = input()
        if choice == "1":
            self.pelear()
        elif choice == "2":
            self.select_arma()
        elif choice == "3":
            self.status()
        elif choice == "4":
            self.salir()
        else:
            print("comando invalido, intenta de nuevo")
            self.bucle()

    def iniciar_personaje(self):
        nickname = input("cual es tu nickname?: ")
        self.nombre = nickname
        self.arma.iniciar()
        self.enemigo.select_enemy()
        self.bucle()

personaje = Personaje()

personaje.iniciar_personaje()