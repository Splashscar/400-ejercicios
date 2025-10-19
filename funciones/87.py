# Este es el archivo n�mero 87
import random

class felipe_mendieta:
    def __init__(self):
        self.num = random.randint(1, 10)

    def intentar(self, intento):
        if intento == self.num:
            return "¡Adivinaste! 🎉"
        elif intento < self.num:
            return "Muy bajo ⬇️"
        else:
            return "Muy alto ⬆️"

juego = felipe_mendieta()
print(juego.intentar(5))
