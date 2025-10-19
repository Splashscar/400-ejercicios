# Este es el archivo n�mero 88
felipe_mendieta = 0
for viaje in range(5):
    km = float(input(f"Kilómetros del viaje {viaje + 1}: "))
    litros = float(input("Litros usados: "))
    rendimiento = km / litros
    print(f"Rendimiento: {rendimiento:.2f} km/l")
    felipe_mendieta += rendimiento

print("Promedio de rendimiento:", felipe_mendieta / 5)
