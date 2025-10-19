# Este es el archivo n�mero 96
class felipe_mendieta:
    def __init__(self, parciales, examen_final):
        self.parciales = parciales
        self.examen_final = examen_final

    def nota_final(self):
        prom = sum(self.parciales) / len(self.parciales)
        final = prom * 0.6 + self.examen_final * 0.4
        print("Nota final:", final)

nota = felipe_mendieta([3.5, 4.0, 4.5], 4.0)
nota.nota_final()
