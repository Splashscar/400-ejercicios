# Este es el archivo n�mero 43
class felipe_mendieta:
    def __init__(self):
        self.precio = 12000
        self.asientos_disponibles = 10

    def comprar(self, cantidad):
        if cantidad > self.asientos_disponibles:
            return "No hay suficientes asientos disponibles."
        self.asientos_disponibles -= cantidad
        total = cantidad * self.precio
        return f"Compra exitosa. Total a pagar: ${total}"

cine = felipe_mendieta()
print(cine.comprar(3))
print("Asientos restantes:", cine.asientos_disponibles)
