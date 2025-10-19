# Este es el archivo n�mero 11
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

rect = felipe_mendieta(10, 5)
print("Perímetro:", rect.perimetro())
