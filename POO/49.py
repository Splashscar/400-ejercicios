# Este es el archivo n�mero 49
class felipe_mendieta:
    def __init__(self, grados):
        self.grados = grados

    def convertir(self):
        f = (self.grados * 9/5) + 32
        print(f"{self.grados}°C = {f}°F")

temp = felipe_mendieta(20)
temp.convertir()
