# Este es el archivo n�mero 54
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto

    def es_mayus(self):
        return self.texto.isupper()

t = felipe_mendieta("PYTHON")
print("¿Está en mayúsculas?", t.es_mayus())
