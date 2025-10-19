# Este es el archivo n�mero 40
class felipe_mendieta:
    def __init__(self, numeros):
        self.numeros = numeros

    def contar_pares(self):
        pares = [n for n in self.numeros if n % 2 == 0]
        impares = [n for n in self.numeros if n % 2 != 0]
        return f"Pares: {len(pares)}, Impares: {len(impares)}"

numeros = felipe_mendieta([1,2,3,4,5,6])
print(numeros.contar_pares())
