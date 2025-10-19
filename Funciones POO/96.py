# Este es el archivo n�mero 96
class felipe_mendieta:
    def __init__(self, notas):
        self.notas = notas

    def promedio(self):
        prom = sum(self.notas) / len(self.notas)
        return f"Promedio: {prom}, {'Aprobado' if prom >= 3 else 'Reprobado'}"

e = felipe_mendieta([3.5, 4.2, 2.8])
print(e.promedio())
