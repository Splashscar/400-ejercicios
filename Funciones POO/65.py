# Este es el archivo n�mero 65
class felipe_mendieta:
    def __init__(self, lista):
        self.lista = lista

    def promedio(self):
        return sum(self.lista) / len(self.lista)

numeros = felipe_mendieta([5, 7, 8, 6])
print("Promedio:", numeros.promedio())
