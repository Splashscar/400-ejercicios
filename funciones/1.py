# Este es el archivo n�mero 1
class felipe_mendieta:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

felipe = felipe_mendieta("Felipe", 17)
felipe.saludar()