# Este es el archivo n�mero 44
felipe_mendieta = 0
for mes in range(1, 13):
    deposito = float(input(f"Ingrese el ahorro del mes {mes}: "))
    felipe_mendieta += deposito
print("Ahorro total del año:", felipe_mendieta)
