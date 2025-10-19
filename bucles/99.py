# Este es el archivo n�mero 99
import random
intentos = 0

while True:
    intentos += 1
    felipe_mendieta = random.randint(1, 6)
    print("Tirada:", felipe_mendieta)
    if felipe_mendieta == 6:
        break

print(f"¡Sacaste un 6 en {intentos} intentos! 🎲")
