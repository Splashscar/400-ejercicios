# Este es el archivo n�mero 76
class felipe_mendieta:
    def __init__(self, precio, iva=0.19):
        self.precio = precio
        self.iva = iva

    def precio_final(self):
        return self.precio * (1 + self.iva)

producto = felipe_mendieta(50000)
print("Precio con IVA:", producto.precio_final())
