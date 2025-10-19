# Este es el archivo n�mero 86
class felipe_mendieta:
    def __init__(self, precio, descuento):
        self.precio = precio
        self.descuento = descuento

    def total(self):
        precio_desc = self.precio * (1 - self.descuento / 100)
        iva = precio_desc * 0.19
        return round(precio_desc + iva, 2)

p = felipe_mendieta(200000, 10)
print("Total con IVA:", p.total())
