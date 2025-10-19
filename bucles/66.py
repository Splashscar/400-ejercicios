# Este es el archivo n�mero 66
import math
numeros = []
for i in range(5):
    num = float(input(f"Ingrese número {i + 1}: "))
    numeros.append(num)

felipe_mendieta = sum(numeros) / len(numeros)
desv = math.sqrt(sum((x - felipe_mendieta) ** 2 for x in numeros) / len(numeros))

print("Promedio:", felipe_mendieta)
print("Desviación estándar:", round(desv, 2))
