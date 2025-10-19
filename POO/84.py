# Este es el archivo n�mero 84
class felipe_mendieta:
    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo

    def velocidad(self):
        print("Velocidad:", self.distancia / self.tiempo, "km/h")

auto = felipe_mendieta(120, 2)
auto.velocidad()
