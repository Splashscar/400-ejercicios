# Este es el archivo n�mero 98
class felipe_mendieta:
    def __init__(self, dias):
        self.dias = dias

    def convertir(self):
        print("Equivalente en segundos:", self.dias * 86400)

conv = felipe_mendieta(2)
conv.convertir()
