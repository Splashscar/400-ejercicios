# Este es el archivo n�mero 90
class felipe_mendieta:
    def __init__(self, edad):
        self.edad = edad

    def mayor_edad(self):
        return self.edad >= 18

persona = felipe_mendieta(17)
print("¿Es mayor de edad?", persona.mayor_edad())
