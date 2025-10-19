# Este es el archivo n�mero 37
class felipe_mendieta:
    def __init__(self, frase):
        self.frase = frase

    def contar(self):
        return len(self.frase)

texto = felipe_mendieta("Python es genial")
print("Cantidad de caracteres:", texto.contar())
