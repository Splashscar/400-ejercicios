# Este es el archivo n�mero 63
class felipe_mendieta:
    def __init__(self, temp):
        self.temp = temp

    def estado(self):
        if self.temp > 25:
            print("Hace calor 🌞")
        elif self.temp < 10:
            print("Hace frío 🥶")
        else:
            print("Clima templado 🌤️")

clima = felipe_mendieta(18)
clima.estado()
