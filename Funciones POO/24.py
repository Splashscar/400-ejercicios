# Este es el archivo n�mero 24
class felipe_mendieta:
    def __init__(self, precios):
        self.precios = precios

    def total(self):
        return sum(self.precios)

compra = felipe_mendieta([12000, 34000, 56000])
print("Total compra:", compra.total())
