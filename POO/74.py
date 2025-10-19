# Este es el archivo n�mero 74
class felipe_mendieta:
    def __init__(self, capital, tasa, meses):
        self.capital = capital
        self.tasa = tasa
        self.meses = meses

    def interes(self):
        interes = self.capital * self.tasa * self.meses / 100
        print("Interés total:", interes)

cuenta = felipe_mendieta(1000000, 1.5, 12)
cuenta.interes()
