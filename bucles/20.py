# Este es el archivo n�mero 20
felipe_mendieta = int(input("Ingrese un número: "))
print("Los divisores de", felipe_mendieta, "son:")
for i in range(1, felipe_mendieta + 1):
    if felipe_mendieta % i == 0:
        print(i)
