# Este es el archivo n�mero 79
class felipe_mendieta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def ahorrar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes.")

    def mostrar(self):
        return f"Saldo actual: ${self.saldo}"

cuenta = felipe_mendieta(100000)
cuenta.ahorrar(50000)
cuenta.retirar(20000)
print(cuenta.mostrar())
