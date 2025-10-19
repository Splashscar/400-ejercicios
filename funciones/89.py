# Este es el archivo n�mero 89
class felipe_mendieta:
    def contar(self, texto):
        palabras = texto.lower().split()
        unicas = set(palabras)
        return f"Palabras únicas: {len(unicas)}"

texto = "El viento susurra y el viento vuelve"
contador = felipe_mendieta()
print(contador.contar(texto))
