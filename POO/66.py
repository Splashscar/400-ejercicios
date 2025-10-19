# Este es el archivo n�mero 66
class felipe_mendieta:
    def __init__(self, edad):
        self.edad = edad

    def validar(self):
        if self.edad >= 18:
            print("Mayor de edad ✅")
        else:
            print("Menor de edad 🚫")

persona = felipe_mendieta(17)
persona.validar()
