# Este es el archivo n�mero 77
class felipe_mendieta:
    def __init__(self, edades):
        self.edades = edades

    def promedio(self):
        return sum(self.edades) / len(self.edades)

grupo = felipe_mendieta([18, 21, 23, 25])
print("Promedio de edades:", grupo.promedio())
