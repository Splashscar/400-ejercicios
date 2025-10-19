# Este es el archivo n�mero 60
class felipe_mendieta:
    def __init__(self, saldo=100000):
        self.saldo = saldo

    def retirar(self, monto):
        if monto > self.saldo:
            return "Fondos insuficientes."
        self.saldo -= monto
        return f"Retiro exitoso. Saldo restante: ${self.saldo}"

    def consultar(self):
        return f"Saldo disponible: ${self.saldo}"

cajero = felipe_mendieta()
print(cajero.retirar(50000))
print(cajero.consultar())
