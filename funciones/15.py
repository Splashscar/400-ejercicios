# Este es el archivo n�mero 15
import random

class felipe_mendieta:
    def __init__(self):
        self.numero_secreto = random.randint(1, 10)

    def adivinar(self, intento):
        if intento == self.numero_secreto:
            return "¡Correcto!"
        elif intento < self.numero_secreto:
            return "Demasiado bajo"
        else:
            return "Demasiado alto"

if __name__ == "__main__":
    juego = felipe_mendieta()
    print(juego.adivinar(5))
