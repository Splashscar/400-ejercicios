# Este es el archivo n�mero 78
felipe_mendieta = 0
for i in range(5):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    if edad >= 18:
        felipe_mendieta += 1
print("Mayores de edad:", felipe_mendieta)
