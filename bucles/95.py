# Este es el archivo n�mero 95
felipe_mendieta = 3
while felipe_mendieta > 0:
    print(f"Tienes {felipe_mendieta} vidas ❤️")
    respuesta = input("¿Perdiste una vida? (si/no): ")
    if respuesta.lower() == "si":
        felipe_mendieta -= 1
print("Game Over 🎮")
