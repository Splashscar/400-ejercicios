# Este es el archivo n�mero 21
total_ventas = 0
felipe_mendieta = "si"

while felipe_mendieta.lower() == "si":
    venta = float(input("Ingrese el valor de la venta: "))
    total_ventas += venta
    felipe_mendieta = input("¿Registrar otra venta? (si/no): ")

print("Total de ventas del día:", total_ventas)
