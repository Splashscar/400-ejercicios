# Este es el archivo n�mero 59
class felipe_mendieta:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad, precio):
        self.productos[nombre] = (cantidad, precio)

    def total(self):
        total = sum(c * p for c, p in self.productos.values())
        print("Valor total del inventario:", total)

inv = felipe_mendieta()
inv.agregar("Monitor", 2, 600000)
inv.agregar("Teclado", 3, 80000)
inv.total()
