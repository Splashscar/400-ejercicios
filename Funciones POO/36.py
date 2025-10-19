# Este es el archivo n�mero 36
class felipe_mendieta:
    def __init__(self, horas):
        self.horas = horas

    def pagar(self):
        tarifa = 2500
        return self.horas * tarifa

carro = felipe_mendieta(5)
print("Pago:", carro.pagar())
