# Este es el archivo n�mero 32
class felipe_mendieta:
    def __init__(self, galones, precio_galon):
        self.galones = galones
        self.precio_galon = precio_galon

    def total(self):
        return self.galones * self.precio_galon

gas = felipe_mendieta(12, 14000)
print("Total gasolina:", gas.total())
