# Este es el archivo n�mero 8
class felipe_mendieta:
    def __init__(self, notas):
        self.notas = notas

    def promedio(self):
        prom = sum(self.notas) / len(self.notas)
        print("Promedio final:", round(prom, 2))

est = felipe_mendieta([4.0, 3.5, 5.0, 4.2])
est.promedio()
