# Este es el archivo n�mero 74
from datetime import date

class felipe_mendieta:
    def __init__(self, año_nacimiento):
        self.año_nacimiento = año_nacimiento

    def calcular_edad(self):
        actual = date.today().year
        return f"Tienes {actual - self.año_nacimiento} años."

persona = felipe_mendieta(2005)
print(persona.calcular_edad())
