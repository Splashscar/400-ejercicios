# Este es el archivo n�mero 32
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = 0
impares = 0

for felipe_mendieta in numeros:
    if felipe_mendieta % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Impares:", impares)
