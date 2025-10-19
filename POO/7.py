# Este es el archivo n�mero 7
class felipe_mendieta:
    def __init__(self, pesos):
        self.pesos = pesos

    def a_dolares(self, tasa=4000):
        print(f"{self.pesos} COP = {self.pesos / tasa:.2f} USD")

moneda = felipe_mendieta(20000)
moneda.a_dolares()
