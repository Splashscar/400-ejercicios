# Este es el archivo n�mero 41
class felipe_mendieta:
    def __init__(self, precio, iva=19):
        self.precio = precio
        self.iva = iva

    def total(self):
        total = self.precio * (1 + self.iva / 100)
        return f"Precio final con IVA ({self.iva}%): ${total}"

producto = felipe_mendieta(1000)
print(producto.total())
