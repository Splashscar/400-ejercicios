# Este es el archivo n�mero 55
class felipe_mendieta:
    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo

    def velocidad(self):
        return self.distancia / self.tiempo

viaje = felipe_mendieta(150, 3)
print("Velocidad promedio:", viaje.velocidad(), "km/h")
