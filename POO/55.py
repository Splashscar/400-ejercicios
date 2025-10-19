# Este es el archivo n�mero 55
class felipe_mendieta:
    def __init__(self):
        self.pedidos = []

    def agregar(self, producto):
        self.pedidos.append(producto)

    def mostrar(self):
        print("Pedidos actuales:", ", ".join(self.pedidos))

pedido = felipe_mendieta()
pedido.agregar("Pizza")
pedido.agregar("Refresco")
pedido.mostrar()
