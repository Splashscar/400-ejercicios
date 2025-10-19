# Este es el archivo n�mero 74
class felipe_mendieta:
    def __init__(self):
        self.productos = []

    def agregar(self, nombre, precio):
        self.productos.append((nombre, precio))

    def total(self):
        return sum(precio for _, precio in self.productos)

carrito = felipe_mendieta()
carrito.agregar("Mouse", 35000)
carrito.agregar("Teclado", 80000)
print("Total del carrito:", carrito.total())
