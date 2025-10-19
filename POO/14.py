# Este es el archivo n�mero 14
class felipe_mendieta:
    def __init__(self, minutos):
        self.minutos = minutos

    def a_horas(self):
        horas = self.minutos // 60
        mins = self.minutos % 60
        print(f"{self.minutos} minutos = {horas}h {mins}min")

tiempo = felipe_mendieta(135)
tiempo.a_horas()
