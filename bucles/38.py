# Este es el archivo n�mero 38
aprobados = 0

for i in range(5):
    felipe_mendieta = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    if felipe_mendieta >= 3.0:
        aprobados += 1

print("Estudiantes aprobados:", aprobados)
