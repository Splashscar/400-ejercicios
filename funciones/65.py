# Este es el archivo n�mero 65
class felipe_mendieta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        prom = sum(self.notas) / len(self.notas)
        estado = "Aprobado ✅" if prom >= 3.0 else "Reprobado ❌"
        return f"{self.nombre} tiene un promedio de {prom:.2f} - {estado}"

estudiante = felipe_mendieta("Felipe")
estudiante.agregar_nota(4.0)
estudiante.agregar_nota(3.8)
estudiante.agregar_nota(2.5)
print(estudiante.promedio())
