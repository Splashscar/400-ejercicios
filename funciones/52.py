# Este es el archivo n�mero 52
class felipe_mendieta:
    def __init__(self):
        self.catalogo = {"GTA V": 80000, "Minecraft": 60000, "FIFA 25": 90000}

    def comprar(self, juego):
        if juego in self.catalogo:
            return f"Has comprado {juego} por ${self.catalogo[juego]}"
        else:
            return "Juego no disponible."

tienda = felipe_mendieta()
print(tienda.comprar("Minecraft"))
