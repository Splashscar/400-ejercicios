# Este es el archivo n�mero 67
class felipe_mendieta:
    def __init__(self, nota):
        self.nota = nota

    def calificar(self):
        if self.nota >= 4.5:
            print("A")
        elif self.nota >= 4.0:
            print("B")
        elif self.nota >= 3.0:
            print("C")
        else:
            print("D")

nota = felipe_mendieta(4.3)
nota.calificar()
