# Este es el archivo n�mero 49
class felipe_mendieta:
    def __init__(self):
        self.productos = {"Camisa": 30000, "Pantalón": 60000, "Zapatos": 80000}
        self.carrito = []

    def comprar(self, producto):
        if producto in self.productos:
            self.carrito.append(self.productos[producto])
        else:
            print("Producto no encontrado.")

    def pagar(self):
        return f"Total de compra: ${sum(self.carrito)}"

tienda = felipe_mendieta()
tienda.comprar("Camisa")
tienda.comprar("Zapatos")
print(tienda.pagar())
