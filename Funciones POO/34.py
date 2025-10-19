# Este es el archivo n�mero 34
class felipe_mendieta:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

cuadro = felipe_mendieta(6)
print("Área:", cuadro.area())
