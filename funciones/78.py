# Este es el archivo n�mero 78
class felipe_mendieta:
    def contar_palabras(self, texto):
        palabras = texto.split()
        return len(palabras)

    def contar_letras(self, texto):
        return len(texto.replace(" ", ""))

analizador = felipe_mendieta()
texto = "Assassin’s Creed es una obra maestra"
print("Palabras:", analizador.contar_palabras(texto))
print("Letras:", analizador.contar_letras(texto))
