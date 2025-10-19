# Este es el archivo n�mero 1
class felipe_mendieta:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, {self.nombre}, bienvenido al mundo POO!")

persona = felipe_mendieta("Camilo")
persona.saludar()
