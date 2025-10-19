# Este es el archivo n�mero 34
productos = [1000, 2500, 8000, 500, 12000, 3000]
limite = 3000
felipe_mendieta = 0

for precio in productos:
    if precio > limite:
        felipe_mendieta += 1

print("Productos con precio mayor a", limite, ":", felipe_mendieta)
