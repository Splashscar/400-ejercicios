# Este es el archivo n�mero 91
class felipe_mendieta:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def evaluar(self):
        if self.nota >= 3:
            print(f"{self.nombre} aprobó 👏")
        else:
            print(f"{self.nombre} reprobó 😔")

alumno = felipe_mendieta("Mateo", 2.5)
alumno.evaluar()
