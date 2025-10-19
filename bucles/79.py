# Este es el archivo n�mero 79
total = 0
for dia in range(1, 8):
    venta = float(input(f"Ingrese las ventas del día {dia}: "))
    total += venta

felipe_mendieta = total / 7
print("Promedio semanal de ventas:", felipe_mendieta)
