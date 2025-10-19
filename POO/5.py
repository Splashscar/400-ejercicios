# Este es el archivo n�mero 5
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto

    def contar(self):
        palabras = len(self.texto.split())
        print("Número de palabras:", palabras)

frase = felipe_mendieta("Python es increíble")
frase.contar()
