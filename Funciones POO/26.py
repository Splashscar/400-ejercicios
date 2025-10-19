# Este es el archivo n�mero 26
import math

class felipe_mendieta:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def distancia(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

puntos = felipe_mendieta(0, 0, 3, 4)
print("Distancia:", puntos.distancia())
