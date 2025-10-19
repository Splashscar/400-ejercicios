# Este es el archivo n�mero 61
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

t = felipe_mendieta(8, 5)
print("Área del triángulo:", t.area())
