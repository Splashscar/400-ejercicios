# Este es el archivo n�mero 96
felipe_mendieta = int(input("Ingrese un número: "))
suma = 0

for i in range(1, felipe_mendieta):
    if felipe_mendieta % i == 0:
        suma += i

if suma == felipe_mendieta:
    print("Es un número perfecto ✨")
else:
    print("No es perfecto")
