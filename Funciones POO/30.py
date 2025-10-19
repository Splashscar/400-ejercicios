# Este es el archivo n�mero 30
class felipe_mendieta:
    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def interes_compuesto(self):
        return self.capital * ((1 + self.tasa / 100) ** self.tiempo)

inversion = felipe_mendieta(1000000, 5, 3)
print("Valor final:", round(inversion.interes_compuesto(), 2))
