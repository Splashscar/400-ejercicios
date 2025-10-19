# Este es el archivo n�mero 33
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto

    def contiene_numeros(self):
        return any(c.isdigit() for c in self.texto)

cadena = felipe_mendieta("Hola123")
print("¿Contiene números?", cadena.contiene_numeros())
