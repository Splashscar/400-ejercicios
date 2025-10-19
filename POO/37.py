# Este es el archivo n�mero 37
class felipe_mendieta:
    def __init__(self, palabra):
        self.palabra = palabra.lower()

    def es_palindromo(self):
        if self.palabra == self.palabra[::-1]:
            print("Es palíndromo")
        else:
            print("No es palíndromo")

pal = felipe_mendieta("radar")
pal.es_palindromo()
