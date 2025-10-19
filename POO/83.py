# Este es el archivo n�mero 83
class felipe_mendieta:
    def __init__(self):
        self.frutas = {}

    def agregar(self, nombre, cantidad):
        self.frutas[nombre] = cantidad

    def mostrar(self):
        for f, c in self.frutas.items():
            print(f"{f}: {c} unidades")

inv = felipe_mendieta()
inv.agregar("Manzanas", 20)
inv.agregar("Bananas", 30)
inv.mostrar()
