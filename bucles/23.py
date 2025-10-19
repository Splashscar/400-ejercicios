# Este es el archivo n�mero 23
suma_edades = 0
cantidad = 0

while True:
    felipe_mendieta = int(input("Ingrese la edad (0 para salir): "))
    if felipe_mendieta == 0:
        break
    suma_edades += felipe_mendieta
    cantidad += 1

if cantidad > 0:
    print("Promedio de edades:", suma_edades / cantidad)
else:
    print("No se ingresaron edades.")
