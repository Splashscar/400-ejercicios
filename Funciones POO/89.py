# Este es el archivo n�mero 89
class felipe_mendieta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            return "Saldo insuficiente"
        self.saldo -= monto
        return "Retiro realizado"

cuenta = felipe_mendieta("Felipe", 100000)
cuenta.depositar(50000)
print("Saldo:", cuenta.saldo)
