# Este es el archivo n�mero 88
class felipe_mendieta:
    def __init__(self, limite):
        self.limite = limite

    def pares(self):
        return [i for i in range(2, self.limite + 1, 2)]

n = felipe_mendieta(20)
print("Pares:", n.pares())
