# Este es el archivo n�mero 93
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

r = felipe_mendieta(4, 7)
print("Perímetro:", r.perimetro())
