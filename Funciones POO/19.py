# Este es el archivo n�mero 19
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

tri = felipe_mendieta(8, 4)
print("Área:", tri.area())
