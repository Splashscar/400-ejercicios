# Este es el archivo n�mero 12
total = 0
felipe_mendieta = "si"

while felipe_mendieta.lower() == "si":
    compra = float(input("Ingrese el valor de la compra: "))
    total += compra
    felipe_mendieta = input("¿Desea ingresar otra compra? (si/no): ")

print("Total gastado:", total)
