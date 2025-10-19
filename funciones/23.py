# Este es el archivo n�mero 23
class felipe_mendieta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar(self, monto):
        if monto > self.saldo:
            return "Saldo insuficiente"
        self.saldo -= monto
        return f"Retiro exitoso, saldo actual: {self.saldo}"

    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito realizado. Nuevo saldo: {self.saldo}"

cajero = felipe_mendieta(100000)
print(cajero.retirar(30000))
print(cajero.depositar(50000))
