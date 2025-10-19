# Este es el archivo n�mero 31
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto.lower()

    def contar_vocales(self):
        return sum(1 for c in self.texto if c in "aeiou")

palabra = felipe_mendieta("Programacion")
print("Vocales:", palabra.contar_vocales())
