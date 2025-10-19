# Este es el archivo n�mero 20
class felipe_mendieta:
    def __init__(self, temperaturas):
        self.temperaturas = temperaturas

    def promedio(self):
        print("Promedio semanal:", sum(self.temperaturas) / len(self.temperaturas))

clima = felipe_mendieta([22, 24, 20, 25, 26, 23, 21])
clima.promedio()
