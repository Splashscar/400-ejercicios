# Este es el archivo n�mero 36
class felipe_mendieta:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def evaluar(self):
        if self.temperatura < 15:
            return "Hace frío 🧣"
        elif self.temperatura <= 25:
            return "Clima agradable 🌤️"
        else:
            return "Hace calor ☀️"

clima = felipe_mendieta(30)
print(clima.evaluar())
