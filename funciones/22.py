# Este es el archivo n�mero 22
import math

class felipe_mendieta:
    def __init__(self):
        pass

    def raiz_cuadrada(self, x):
        return math.sqrt(x)

    def potencia(self, base, exponente):
        return pow(base, exponente)

    def seno(self, angulo):
        return math.sin(math.radians(angulo))

calc = felipe_mendieta()
print(calc.raiz_cuadrada(25))
print(calc.potencia(2, 4))
print(calc.seno(30))
