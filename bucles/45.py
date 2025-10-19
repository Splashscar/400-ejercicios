# Este es el archivo n�mero 45
palabra = input("Ingrese una palabra: ").lower()
vocales = "aeiou"
felipe_mendieta = 0

for letra in palabra:
    if letra in vocales:
        felipe_mendieta += 1
print("Cantidad de vocales:", felipe_mendieta)
