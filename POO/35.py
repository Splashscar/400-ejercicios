# Este es el archivo n�mero 35
class felipe_mendieta:
    def __init__(self, texto, veces):
        self.texto = texto
        self.veces = veces

    def repetir(self):
        for _ in range(self.veces):
            print(self.texto)

msg = felipe_mendieta("Aprendiendo Python", 3)
msg.repetir()
