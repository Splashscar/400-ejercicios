# Este es el archivo n�mero 47
felipe_mendieta = 0
while True:
    factura = float(input("Ingrese valor de factura (0 para salir): "))
    if factura == 0:
        break
    felipe_mendieta += factura
print("Total de facturas:", felipe_mendieta)
