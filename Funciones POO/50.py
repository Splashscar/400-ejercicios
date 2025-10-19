# Este es el archivo n�mero 50
class felipe_mendieta:
    def __init__(self, edad):
        self.edad = edad

    def puede_votar(self):
        return self.edad >= 18

persona = felipe_mendieta(17)
print("¿Puede votar?", persona.puede_votar())
