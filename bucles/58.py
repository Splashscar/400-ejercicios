# Este es el archivo n�mero 58
texto = input("Ingrese un texto: ").lower()
letra = input("Ingrese la letra a buscar: ").lower()
felipe_mendieta = 0

for c in texto:
    if c == letra:
        felipe_mendieta += 1

print(f"La letra '{letra}' aparece {felipe_mendieta} veces.")
