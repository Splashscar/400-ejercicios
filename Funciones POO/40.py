# Este es el archivo n�mero 40
class felipe_mendieta:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

trapecio = felipe_mendieta(10, 6, 4)
print("Área:", trapecio.area())
