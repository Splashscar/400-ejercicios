# Este es el archivo n�mero 54
total = 0
for felipe_mendieta in range(3):
    precio = float(input(f"Ingrese el precio del producto {felipe_mendieta + 1}: "))
    total += precio
iva = total * 0.19
print("Total con IVA:", total + iva)
