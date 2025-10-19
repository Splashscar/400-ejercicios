# Este es el archivo n�mero 38
class felipe_mendieta:
    def __init__(self, texto):
        self.texto = texto

    def contar(self):
        print("Número de caracteres:", len(self.texto))

t = felipe_mendieta("Programar es arte")
t.contar()
