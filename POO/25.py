# Este es el archivo n�mero 25
class felipe_mendieta:
    def __init__(self, precio, descuento):
        self.precio = precio
        self.descuento = descuento

    def aplicar_descuento(self):
        nuevo = self.precio - (self.precio * self.descuento / 100)
        print("Precio con descuento:", nuevo)

producto = felipe_mendieta(120000, 15)
producto.aplicar_descuento()
