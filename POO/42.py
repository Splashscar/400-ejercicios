# Este es el archivo n�mero 42
class felipe_mendieta:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro exitoso. Saldo actual:", self.saldo)
        else:
            print("Saldo insuficiente.")

atm = felipe_mendieta(1000000)
atm.retirar(250000)
