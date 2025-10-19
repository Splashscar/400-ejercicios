# Este es el archivo n�mero 83
class felipe_mendieta:
    def __init__(self, frase):
        self.frase = frase

    def contar_palabras(self):
        return len(self.frase.split())

f = felipe_mendieta("Hoy el código fluye como un río de bits")
print("Palabras:", f.contar_palabras())
