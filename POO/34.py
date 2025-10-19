# Este es el archivo n�mero 34
class felipe_mendieta:
    def __init__(self, nota):
        self.nota = nota

    def evaluar(self):
        if self.nota >= 3:
            print("Aprobado")
        else:
            print("Reprobado")

examen = felipe_mendieta(2.9)
examen.evaluar()
