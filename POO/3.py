# Este es el archivo n�mero 3
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print("Área del rectángulo:", self.base * self.altura)

figura = felipe_mendieta(10, 4)
figura.area()
