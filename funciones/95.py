# Este es el archivo n�mero 95
class felipe_mendieta:
    def calcular(self, notas, pesos):
        suma = sum(n * p for n, p in zip(notas, pesos))
        total_pesos = sum(pesos)
        return suma / total_pesos

prom = felipe_mendieta()
print("Promedio ponderado:", prom.calcular([3.5, 4.0, 5.0], [0.2, 0.3, 0.5]))
