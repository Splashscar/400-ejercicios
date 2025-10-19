# Este es el archivo n�mero 76
class felipe_mendieta:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def convertir(self):
        print(f"{self.cantidad} USD = {self.cantidad * 3950} COP")

usd = felipe_mendieta(5)
usd.convertir()
