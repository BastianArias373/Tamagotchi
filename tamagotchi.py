class Tamagochi:

    def __init__(self,nombre,humor):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = humor
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f"nombre: {self.nombre}")
        print(f"energia: {self.nivel_energia}%")

    def alimentar(self):
        self.nivel_hambre -= 10
        self.nivel_energia += 15

    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10

    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5

    def verificar_estado(self):
        if self.nivel_energia > 0:
            self.esta_vivo = True
        else:
            self.esta_vivo = False

tama1 = Tamagochi("Tama1","Feliz")
tama1.mostrar_estado()
