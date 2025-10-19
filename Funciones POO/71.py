# Este es el archivo n�mero 71
class felipe_mendieta:
    def __init__(self, edad):
        self.edad = edad

    def años_restantes(self):
        return max(0, 65 - self.edad)

persona = felipe_mendieta(40)
print("Años para jubilarse:", persona.años_restantes())
