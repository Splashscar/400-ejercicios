# Este es el archivo n�mero 28
felipe_mendieta = 0
while True:
    entrada = input("¿Entró un auto? (si/no): ").lower()
    if entrada == "si":
        felipe_mendieta += 1
    else:
        break
print("Autos registrados:", felipe_mendieta)
