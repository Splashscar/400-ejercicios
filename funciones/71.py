# Este es el archivo n�mero 71
class felipe_mendieta:
    def __init__(self, cliente, monto, interes):
        self.cliente = cliente
        self.monto = monto
        self.interes = interes

    def calcular_total(self):
        total = self.monto * (1 + self.interes / 100)
        return f"{self.cliente} debe pagar ${total}"

prestamo = felipe_mendieta("Felipe", 1000000, 10)
print(prestamo.calcular_total())
