# Este es el archivo n�mero 12
class felipe_mendieta:
    def __init__(self, segundos):
        self.segundos = segundos

    def convertir(self):
        return self.segundos / 60

tiempo = felipe_mendieta(180)
print("Minutos:", tiempo.convertir())
