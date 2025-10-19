# Este es el archivo n�mero 53
class felipe_mendieta:
    def __init__(self, precio, descuento):
        self.precio = precio
        self.descuento = descuento

    def precio_final(self):
        return self.precio * (1 - self.descuento / 100)

p = felipe_mendieta(100000, 15)
print("Precio con descuento:", p.precio_final())
