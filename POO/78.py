# Este es el archivo n�mero 78
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print("Área:", (self.base * self.altura) / 2)

triangulo = felipe_mendieta(10, 5)
triangulo.area()
