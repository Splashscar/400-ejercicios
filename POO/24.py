# Este es el archivo n�mero 24
class felipe_mendieta:
    def __init__(self, dias):
        self.dias = dias

    def convertir(self):
        semanas = self.dias // 7
        resto = self.dias % 7
        print(f"{self.dias} días = {semanas} semanas y {resto} días")

tiempo = felipe_mendieta(45)
tiempo.convertir()
