# Este es el archivo n�mero 87
suma = 0
contador = 0

while True:
    felipe_mendieta = int(input("Ingrese edad (-1 para terminar): "))
    if felipe_mendieta == -1:
        break
    suma += felipe_mendieta
    contador += 1

if contador > 0:
    print("Promedio de edades:", suma / contador)
else:
    print("No se ingresaron edades.")
