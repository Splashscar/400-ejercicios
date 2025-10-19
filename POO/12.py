# Este es el archivo n�mero 12
class felipe_mendieta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print("Depósito exitoso. Saldo:", self.saldo)

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retiro exitoso. Saldo:", self.saldo)
        else:
            print("Fondos insuficientes.")

cuenta = felipe_mendieta(1000)
cuenta.depositar(500)
cuenta.retirar(300)
