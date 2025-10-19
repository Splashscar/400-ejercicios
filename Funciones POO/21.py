# Este es el archivo n�mero 21
from datetime import date

class felipe_mendieta:
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        return date.today().year - self.nacimiento

persona = felipe_mendieta(2005)
print("Edad:", persona.edad())
