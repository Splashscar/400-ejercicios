# Este es el archivo n�mero 47
class felipe_mendieta:
    def __init__(self, precio, porcentaje):
        self.precio = precio
        self.porcentaje = porcentaje

    def total(self):
        descuento = self.precio * self.porcentaje / 100
        total = self.precio - descuento
        print(f"Total con descuento: ${total}")

compra = felipe_mendieta(250000, 10)
compra.total()
