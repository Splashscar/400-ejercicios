# Este es el archivo n�mero 2
import math

class felipe_mendieta:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

circulo = felipe_mendieta(5)
print("Área:", round(circulo.area(), 2))
