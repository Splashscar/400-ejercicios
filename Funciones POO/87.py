# Este es el archivo n�mero 87
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self):
        return len(self.texto.split())

f = felipe_mendieta("El conocimiento es poder")
print("Cantidad de palabras:", f.contar_palabras())
