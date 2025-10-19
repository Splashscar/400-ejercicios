# Este es el archivo n�mero 44
class felipe_mendieta:
    def __init__(self, materia):
        self.materia = materia
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        prom = sum(self.notas) / len(self.notas)
        print(f"Promedio de {self.materia}: {prom:.2f}")

mate = felipe_mendieta("Matemáticas")
mate.agregar_nota(4.5)
mate.agregar_nota(3.9)
mate.promedio()
