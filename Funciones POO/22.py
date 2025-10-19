# Este es el archivo n�mero 22
class felipe_mendieta:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

lista = felipe_mendieta([2, 4, 6, 8, 10])
print("Promedio:", lista.promedio())
