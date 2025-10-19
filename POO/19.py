# Este es el archivo n�mero 19
class felipe_mendieta:
    def __init__(self, lista):
        self.lista = lista

    def contar_pares(self):
        pares = [n for n in self.lista if n % 2 == 0]
        print("Números pares:", pares)

nums = felipe_mendieta([1, 2, 3, 4, 5, 6])
nums.contar_pares()
