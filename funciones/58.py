# Este es el archivo n�mero 58
class felipe_mendieta:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def estado(self):
        if self.temperatura > 40:
            return "🔥 Alerta: temperatura muy alta"
        elif self.temperatura < 10:
            return "❄️ Temperatura muy baja"
        else:
            return "🌡️ Temperatura estable"

sensor = felipe_mendieta(25)
print(sensor.estado())
