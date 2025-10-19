# Este es el archivo n�mero 26
class felipe_mendieta:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def mostrar(self):
        print("Inventario:")
        for nombre, cantidad in self.productos.items():
            print(f"{nombre}: {cantidad}")

inv = felipe_mendieta()
inv.agregar("Teclado", 5)
inv.agregar("Mouse", 3)
inv.mostrar()
