# Este es el archivo n�mero 63
capital = float(input("Ingrese el capital inicial: "))
tasa = 0.05

for felipe_mendieta in range(1, 6):
    capital *= 1 + tasa
    print(f"Año {felipe_mendieta}: ${round(capital, 2)}")
