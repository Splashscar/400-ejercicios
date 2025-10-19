# Este es el archivo n�mero 25
class felipe_mendieta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def agregar_item(self, descripcion, precio):
        self.items.append((descripcion, precio))

    def total(self):
        return sum(precio for _, precio in self.items)

factura = felipe_mendieta("Felipe")
factura.agregar_item("Mouse", 50)
factura.agregar_item("Teclado", 100)
print("Total de la factura:", factura.total())
