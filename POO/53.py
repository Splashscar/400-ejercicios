# Este es el archivo n�mero 53
class felipe_mendieta:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def evaluar(self):
        if self.nota >= 3:
            print(f"{self.nombre} aprobó")
        else:
            print(f"{self.nombre} reprobó")

alumno = felipe_mendieta("Juan", 2.8)
alumno.evaluar()
