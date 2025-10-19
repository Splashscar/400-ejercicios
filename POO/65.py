# Este es el archivo n�mero 65
class felipe_mendieta:
    def __init__(self):
        self.notas = []

    def agregar(self, n):
        self.notas.append(n)

    def promedio(self):
        print("Promedio:", sum(self.notas) / len(self.notas))

curso = felipe_mendieta()
curso.agregar(4.0)
curso.agregar(3.8)
curso.agregar(4.5)
curso.promedio()
