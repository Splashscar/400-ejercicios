# Este es el archivo n�mero 29
felipe_mendieta = 1000
tasa = 0.1

for año in range(1, 6):
    felipe_mendieta += felipe_mendieta * tasa
    print(f"Año {año}: {int(felipe_mendieta)} habitantes")
