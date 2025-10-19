# Este es el archivo n�mero 86
import random
contador = 0

for felipe_mendieta in range(10):
    tiro = random.randint(1, 6)
    print("Tiro:", tiro)
    if tiro == 6:
        contador += 1
print("Veces que salió 6:", contador)
