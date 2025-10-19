# Este es el archivo n�mero 51
class felipe_mendieta:
    def __init__(self, n):
        self.n = n

    def pares(self):
        return [i for i in range(self.n + 1) if i % 2 == 0]

numeros = felipe_mendieta(10)
print("Pares:", numeros.pares())
