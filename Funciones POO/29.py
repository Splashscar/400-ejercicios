# Este es el archivo n�mero 29
class felipe_mendieta:
    def __init__(self, metros):
        self.metros = metros

    def convertir(self):
        return self.metros * 100

longitud = felipe_mendieta(5)
print("Centímetros:", longitud.convertir())
