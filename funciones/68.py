# Este es el archivo n�mero 68
class felipe_mendieta:
    def __init__(self, ciudad, temperatura):
        self.ciudad = ciudad
        self.temperatura = temperatura

    def analizar(self):
        if self.temperatura > 30:
            return f"{self.ciudad}: Calor extremo ☀️"
        elif self.temperatura < 10:
            return f"{self.ciudad}: Frío intenso ❄️"
        else:
            return f"{self.ciudad}: Clima agradable 🌤️"

clima = felipe_mendieta("Bogotá", 22)
print(clima.analizar())
