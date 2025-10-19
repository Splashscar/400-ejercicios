# Este es el archivo n�mero 29
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto.lower()

    def contar_vocales(self):
        contador = sum(1 for letra in self.texto if letra in "aeiou")
        print("Número de vocales:", contador)

frase = felipe_mendieta("Hola Mundo")
frase.contar_vocales()
