# Este es el archivo n�mero 92
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto

    def tiene_numeros(self):
        return any(c.isdigit() for c in self.texto)

t = felipe_mendieta("Python3")
print("¿Contiene números?", t.tiene_numeros())
