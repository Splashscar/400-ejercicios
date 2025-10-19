# Este es el archivo n�mero 49
class felipe_mendieta:
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def potencia(self):
        return self.base ** self.exponente

p = felipe_mendieta(3, 4)
print("Potencia:", p.potencia())
