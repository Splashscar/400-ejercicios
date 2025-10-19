# Este es el archivo n�mero 30
class felipe_mendieta:
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def potencia(self):
        print("Resultado:", self.base ** self.exponente)

calc = felipe_mendieta(2, 5)
calc.potencia()
