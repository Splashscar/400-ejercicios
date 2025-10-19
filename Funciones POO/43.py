# Este es el archivo n�mero 43
class felipe_mendieta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

cuenta = felipe_mendieta(50000)
cuenta.depositar(30000)
cuenta.retirar(20000)
print("Saldo final:", cuenta.saldo)
