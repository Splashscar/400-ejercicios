# Este es el archivo n�mero 27
felipe_mendieta = 1000  # capital inicial
interes = 0.05
for año in range(1, 6):
    felipe_mendieta += felipe_mendieta * interes
    print(f"Año {año}: ${round(felipe_mendieta, 2)}")
