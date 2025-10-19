# Este es el archivo n�mero 90
class felipe_mendieta:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, precio):
        self.productos[nombre] = precio

    def total(self):
        print("Valor total:", sum(self.productos.values()))

inv = felipe_mendieta()
inv.agregar("Mouse", 50000)
inv.agregar("Teclado", 80000)
inv.total()
