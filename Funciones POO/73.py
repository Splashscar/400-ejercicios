# Este es el archivo n�mero 73
class felipe_mendieta:
    def __init__(self, lista):
        self.lista = lista

    def mayores(self):
        return len([n for n in self.lista if n > 10])

lista = felipe_mendieta([3, 15, 8, 22, 9])
print("Mayores que 10:", lista.mayores())
