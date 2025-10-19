# Este es el archivo n�mero 67
class felipe_mendieta:
    def __init__(self):
        self.catalogo = {"Teclado": 45000, "Mouse": 25000, "Monitor": 300000}
        self.carrito = []

    def agregar_producto(self, producto):
        if producto in self.catalogo:
            self.carrito.append(producto)
        else:
            print("Producto no disponible.")

    def pagar(self):
        total = sum(self.catalogo[p] for p in self.carrito)
        return f"Total a pagar: ${total}"

tienda = felipe_mendieta()
tienda.agregar_producto("Mouse")
tienda.agregar_producto("Teclado")
print(tienda.pagar())
