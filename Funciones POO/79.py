# Este es el archivo n�mero 79
class felipe_mendieta:
    def __init__(self, segundos):
        self.segundos = segundos

    def convertir(self):
        horas = self.segundos // 3600
        minutos = (self.segundos % 3600) // 60
        seg = self.segundos % 60
        return horas, minutos, seg

t = felipe_mendieta(3670)
print("Tiempo (h, m, s):", t.convertir())
