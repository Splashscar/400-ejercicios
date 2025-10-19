# Este es el archivo n�mero 76
class felipe_mendieta:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def eliminar(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]

    def mostrar(self):
        for p, c in self.productos.items():
            print(f"{p}: {c} unidades")

inv = felipe_mendieta()
inv.agregar("Teclados", 10)
inv.agregar("Monitores", 5)
inv.mostrar()
