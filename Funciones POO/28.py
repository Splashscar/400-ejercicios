# Este es el archivo n�mero 28
class felipe_mendieta:
    def __init__(self, palabra):
        self.palabra = palabra

    def es_palindromo(self):
        p = self.palabra.replace(" ", "").lower()
        return p == p[::-1]

texto = felipe_mendieta("Anita lava la tina")
print("¿Es palíndromo?", texto.es_palindromo())
