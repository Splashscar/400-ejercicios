# Este es el archivo n�mero 34
class felipe_mendieta:
    def __init__(self, precio, descuento):
        self.precio = precio
        self.descuento = descuento

    def total(self):
        valor_final = self.precio - (self.precio * self.descuento / 100)
        return f"Precio final: ${valor_final}"

producto = felipe_mendieta(200, 10)
print(producto.total())
