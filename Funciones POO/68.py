# Este es el archivo n�mero 68
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def doble_triple(self):
        return (self.numero * 2, self.numero * 3)

n = felipe_mendieta(7)
print("Doble y triple:", n.doble_triple())
