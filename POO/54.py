# Este es el archivo n�mero 54
from datetime import date
class felipe_mendieta:
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        hoy = date.today().year
        print("Edad:", hoy - self.nacimiento)

persona = felipe_mendieta(2003)
persona.edad()
