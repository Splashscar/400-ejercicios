# Este es el archivo n�mero 16
class felipe_mendieta:
    def __init__(self, notas, pesos):
        self.notas = notas
        self.pesos = pesos

    def promedio_ponderado(self):
        total = sum(n * p for n, p in zip(self.notas, self.pesos))
        print("Promedio ponderado:", round(total / sum(self.pesos), 2))

alumno = felipe_mendieta([4.5, 3.8, 4.0], [0.3, 0.3, 0.4])
alumno.promedio_ponderado()
