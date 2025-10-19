# Este es el archivo n�mero 15
class felipe_mendieta:
    def __init__(self, frase):
        self.frase = frase

    def contar_palabras(self):
        return len(self.frase.split())

texto = felipe_mendieta("Aprender Python es divertido")
print("Palabras:", texto.contar_palabras())
