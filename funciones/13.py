# Este es el archivo n�mero 13
class felipe_mendieta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= cantidad

    def mostrar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self.saldo}"

if __name__ == "__main__":
    cuenta = felipe_mendieta("Felipe", 1000)
    cuenta.depositar(500)
    cuenta.retirar(200)
    print(cuenta.mostrar_saldo())
