# Este es el archivo n�mero 44
class felipe_mendieta:
    def __init__(self, frase):
        self.frase = frase

    def contar_palabras(self):
        return len(self.frase.split())

f = felipe_mendieta("El código también es poesía")
print("Palabras:", f.contar_palabras())
