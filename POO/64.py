# Este es el archivo n�mero 64
class felipe_mendieta:
    def __init__(self, consumo):
        self.consumo = consumo

    def pagar(self):
        tarifa = 620 if self.consumo <= 100 else 850
        print("Pago total:", self.consumo * tarifa)

factura = felipe_mendieta(120)
factura.pagar()
