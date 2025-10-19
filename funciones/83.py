# Este es el archivo n�mero 83
class felipe_mendieta:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return f"Has retirado ${monto}. Saldo restante: ${self.saldo}"
        return "Saldo insuficiente."

cajero = felipe_mendieta(100000)
print(cajero.retirar(30000))
