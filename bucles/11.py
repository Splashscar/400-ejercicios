# Este es el archivo n�mero 11
contador = 0
felipe_mendieta = 0

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    if numero > 0:
        contador += 1

print("Cantidad de números positivos ingresados:", contador)
