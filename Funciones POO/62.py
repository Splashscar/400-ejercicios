# Este es el archivo n�mero 62
class felipe_mendieta:
    def __init__(self, metros):
        self.metros = metros

    def convertir(self):
        return self.metros * 100

c = felipe_mendieta(1.75)
print("Centímetros:", c.convertir())
