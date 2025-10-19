# Este es el archivo n�mero 98
class felipe_mendieta:
    def __init__(self):
        self.items = {}

    def agregar(self, nombre, cantidad):
        self.items[nombre] = self.items.get(nombre, 0) + cantidad

    def mostrar(self):
        for k, v in self.items.items():
            print(f"{k}: {v} unidades")

inv = felipe_mendieta()
inv.agregar("Mouse", 3)
inv.agregar("Teclado", 2)
inv.mostrar()
