# Este es el archivo n�mero 17
class felipe_mendieta:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, producto, precio):
        self.carrito.append({"producto": producto, "precio": precio})

    def total(self):
        return sum(item["precio"] for item in self.carrito)

if __name__ == "__main__":
    carrito = felipe_mendieta()
    carrito.agregar_producto("Mouse", 40)
    carrito.agregar_producto("Teclado", 70)
    print("Total:", carrito.total())
