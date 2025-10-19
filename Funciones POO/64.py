# Este es el archivo n�mero 64
class felipe_mendieta:
    def __init__(self, palabra):
        self.palabra = palabra

    def contar_vocales(self):
        return sum(1 for letra in self.palabra.lower() if letra in "aeiou")

p = felipe_mendieta("Programador")
print("Vocales:", p.contar_vocales())
