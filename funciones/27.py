# Este es el archivo n�mero 27
class felipe_mendieta:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def evaluar(self):
        if self.temperatura > 37:
            return "Tienes fiebre 😷"
        elif self.temperatura < 35:
            return "Tienes hipotermia ❄️"
        else:
            return "Temperatura normal ✅"

termometro = felipe_mendieta(38)
print(termometro.evaluar())
