# Este es el archivo n�mero 100
class felipe_mendieta:
    def __init__(self, distancia, velocidad):
        self.distancia = distancia
        self.velocidad = velocidad

    def tiempo(self):
        print("Tiempo de viaje:", self.distancia / self.velocidad, "horas")

viaje = felipe_mendieta(300, 100)
viaje.tiempo()
