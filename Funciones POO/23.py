# Este es el archivo n�mero 23
class felipe_mendieta:
    def __init__(self, horas):
        self.horas = horas

    def segundos(self):
        return self.horas * 3600

tiempo = felipe_mendieta(2)
print("Segundos:", tiempo.segundos())
