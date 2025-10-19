# Este es el archivo n�mero 71
felipe_mendieta = 0

while True:
    precio = float(input("Ingrese el precio del producto (0 para terminar): "))
    if precio == 0:
        break
    felipe_mendieta += precio

print("Total de la compra:", felipe_mendieta)
