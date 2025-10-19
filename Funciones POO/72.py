# Este es el archivo n�mero 72
class felipe_mendieta:
    def __init__(self, n):
        self.n = n

    def cuadrados(self):
        return [i**2 for i in range(1, self.n + 1)]

l = felipe_mendieta(5)
print("Cuadrados:", l.cuadrados())
