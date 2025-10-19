# Este es el archivo n�mero 14
class felipe_mendieta:
    def __init__(self, valor, descuento):
        self.valor = valor
        self.descuento = descuento

    def total(self):
        return self.valor - (self.valor * self.descuento / 100)

compra = felipe_mendieta(200000, 15)
print("Total con descuento:", compra.total())
