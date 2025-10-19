# Este es el archivo n�mero 82
contador = 0
for felipe_mendieta in range(1, 51):
    if felipe_mendieta % 4 == 0 or felipe_mendieta % 6 == 0:
        contador += 1
print("Cantidad de números divisibles por 4 o 6:", contador)
