# Este es el archivo n�mero 48
class felipe_mendieta:
    def __init__(self):
        self.menu = {"Hamburguesa": 15000, "Perro caliente": 10000, "Papas": 7000}
        self.pedido = []

    def agregar_pedido(self, producto):
        if producto in self.menu:
            self.pedido.append(producto)
        else:
            print("Producto no disponible.")

    def total(self):
        return sum(self.menu[p] for p in self.pedido)

restaurante = felipe_mendieta()
restaurante.agregar_pedido("Hamburguesa")
restaurante.agregar_pedido("Papas")
print("Total a pagar:", restaurante.total())
