# Este es el archivo n�mero 35
class felipe_mendieta:
    def __init__(self, precio, descuento):
        self.precio = precio
        self.descuento = descuento

    def total(self):
        valor_desc = self.precio * (1 - self.descuento / 100)
        return valor_desc * 1.19

venta = felipe_mendieta(100000, 10)
print("Total final:", round(venta.total(), 2))
