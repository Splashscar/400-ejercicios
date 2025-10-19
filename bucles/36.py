# Este es el archivo n�mero 36
palabra_secreta = "python"
intento = ""
felipe_mendieta = 0

while intento != palabra_secreta:
    intento = input("Adivina la palabra: ").lower()
    felipe_mendieta += 1

print(f"¡Correcto! Lo lograste en {felipe_mendieta} intentos.")
