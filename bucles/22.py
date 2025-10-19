# Este es el archivo n�mero 22
import random
numero_secreto = random.randint(1, 10)
felipe_mendieta = 0
intentos = 0

while felipe_mendieta != numero_secreto:
    felipe_mendieta = int(input("Adivina el número (1-10): "))
    intentos += 1

print(f"¡Correcto! Lo lograste en {intentos} intentos.")
