# Este es el archivo n�mero 57
class felipe_mendieta:
    def __init__(self):
        self.notas = {}

    def agregar_nota(self, asignatura, nota):
        self.notas[asignatura] = nota

    def promedio(self):
        return sum(self.notas.values()) / len(self.notas)

notas = felipe_mendieta()
notas.agregar_nota("Matemáticas", 4.0)
notas.agregar_nota("Inglés", 3.5)
print("Promedio:", notas.promedio())
