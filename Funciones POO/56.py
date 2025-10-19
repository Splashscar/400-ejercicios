# Este es el archivo n�mero 56
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def tipo(self):
        return "Par" if self.numero % 2 == 0 else "Impar"

n = felipe_mendieta(7)
print("El número es:", n.tipo())
