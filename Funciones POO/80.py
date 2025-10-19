# Este es el archivo n�mero 80
class felipe_mendieta:
    def __init__(self, productos):
        self.productos = productos

    def total_factura(self):
        subtotal = sum(precio for _, precio in self.productos)
        iva = subtotal * 0.19
        return subtotal + iva

factura = felipe_mendieta([("Pan", 2000), ("Leche", 3000), ("Huevos", 6000)])
print("Total factura:", factura.total_factura())
