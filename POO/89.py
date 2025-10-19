# Este es el archivo n�mero 89
class felipe_mendieta:
    def __init__(self):
        self.estudiantes = []

    def agregar(self, nombre):
        self.estudiantes.append(nombre)

    def mostrar(self):
        for e in self.estudiantes:
            print(e)

grupo = felipe_mendieta()
grupo.agregar("Camila")
grupo.agregar("Santiago")
grupo.mostrar()
