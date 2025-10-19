# Este es el archivo n�mero 27
class felipe_mendieta:
    def __init__(self, cantidad, precio):
        self.cantidad = cantidad
        self.precio = precio

    def total(self):
        return self.cantidad * self.precio

cine = felipe_mendieta(3, 12000)
print("Total a pagar:", cine.total())
