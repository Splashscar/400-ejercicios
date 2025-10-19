# Este es el archivo n�mero 94
class felipe_mendieta:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def verificar(self):
        for p, c in self.productos.items():
            if c == 0:
                print(f"{p} está agotado 🚫")
            else:
                print(f"{p}: {c} disponibles ✅")

tienda = felipe_mendieta()
tienda.agregar("Leche", 5)
tienda.agregar("Pan", 0)
tienda.verificar()
