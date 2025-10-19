# Este es el archivo n�mero 6
class felipe_mendieta:
    def __init___(self, texto):
        self.texto = texto
    def contar_vocales(self):
        vocales = "aeiouAEIOU"
        contador = 0
        for char in self.texto:
            if char in vocales:
                contador += 1
        return contador
frase = "Hola, este es un ejemplo de conteo de vocales."
contador_vocales = felipe_mendieta(frase)
resultado = contador_vocales.contar_vocales()
print(f"El número de vocales en la frase es: {resultado}")