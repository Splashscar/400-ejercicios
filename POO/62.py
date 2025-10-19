# Este es el archivo n�mero 62
class felipe_mendieta:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def listar(self):
        print("Inventario:", ", ".join(self.items))

inv = felipe_mendieta()
inv.agregar("Mouse")
inv.agregar("Teclado")
inv.listar()
