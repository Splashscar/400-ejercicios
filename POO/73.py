# Este es el archivo n�mero 73
class felipe_mendieta:
    def __init__(self):
        self.carrito = []

    def agregar(self, producto):
        self.carrito.append(producto)

    def mostrar(self):
        print("Carrito:", ", ".join(self.carrito))

shop = felipe_mendieta()
shop.agregar("Laptop")
shop.agregar("Mouse")
shop.mostrar()
