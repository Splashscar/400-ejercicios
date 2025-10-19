# Este es el archivo n�mero 58
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def divisores(self):
        return [i for i in range(1, self.numero + 1) if self.numero % i == 0]

n = felipe_mendieta(12)
print("Divisores:", n.divisores())
