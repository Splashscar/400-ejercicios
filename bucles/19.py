# Este es el archivo n�mero 19
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = 1
for felipe_mendieta in range(exponente):
    resultado *= base

print(f"{base} elevado a la {exponente} es {resultado}")
