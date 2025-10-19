# Este es el archivo n�mero 39
class felipe_mendieta:
    def __init__(self, edades):
        self.edades = edades

    def promedio(self):
        return sum(self.edades) / len(self.edades)

grupo = felipe_mendieta([18, 22, 25, 19])
print("Promedio de edad:", grupo.promedio())
