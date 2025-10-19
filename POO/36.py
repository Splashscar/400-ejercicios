# Este es el archivo n�mero 36
class felipe_mendieta:
    def __init__(self, edades):
        self.edades = edades

    def promedio(self):
        prom = sum(self.edades) / len(self.edades)
        print("Edad promedio:", prom)

grupo = felipe_mendieta([18, 22, 25, 19, 21])
grupo.promedio()
