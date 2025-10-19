# Este es el archivo n�mero 67
import random
cara, sello = 0, 0

for felipe_mendieta in range(10):
    if random.choice(["cara", "sello"]) == "cara":
        cara += 1
    else:
        sello += 1

print("Caras:", cara, "| Sellos:", sello)
