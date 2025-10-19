# Este es el archivo n�mero 59
class felipe_mendieta:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, precio):
        self.items.append((nombre, precio))

    def total(self):
        subtotal = sum(p for _, p in self.items)
        iva = subtotal * 0.19
        return f"Subtotal: ${subtotal}, IVA: ${iva}, Total: ${subtotal + iva}"

factura = felipe_mendieta()
factura.agregar_item("Teclado", 50000)
factura.agregar_item("Mouse", 30000)
print(factura.total())
