# Este es el archivo n�mero 57
import random
numero = random.randint(1, 10)
intento = 0
felipe_mendieta = 5

while intento < felipe_mendieta:
    intento += 1
    n = int(input("Adivina el número (1-10): "))
    if n == numero:
        print("¡Correcto!")
        break
    else:
        print("Incorrecto.")
else:
    print("Perdiste, el número era:", numero)
