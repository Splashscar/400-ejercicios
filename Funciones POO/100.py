# Este es el archivo n�mero 100
class felipe_mendieta:
    def __init__(self, notas, pesos):
        self.notas = notas
        self.pesos = pesos

    def nota_final(self):
        total = sum(n * p for n, p in zip(self.notas, self.pesos))
        return round(total / sum(self.pesos), 2)

alumno = felipe_mendieta([4.5, 3.8, 5.0], [0.3, 0.3, 0.4])
print("Nota final:", alumno.nota_final())
