# Este es el archivo n�mero 21
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print("Área del triángulo:", (self.base * self.altura) / 2)

figura = felipe_mendieta(10, 5)
figura.area()
