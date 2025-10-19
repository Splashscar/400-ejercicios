# Este es el archivo n�mero 84
class felipe_mendieta:
    def __init__(self, notas):
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

notas = felipe_mendieta([4.0, 3.5, 5.0, 4.2])
print("Promedio:", notas.promedio())
