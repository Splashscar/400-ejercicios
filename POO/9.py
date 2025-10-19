# Este es el archivo n�mero 9
class felipe_mendieta:
    def __init__(self, edad):
        self.edad = edad

    def verificar(self):
        if self.edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")

persona = felipe_mendieta(20)
persona.verificar()
