# Este es el archivo n�mero 14
class felipe_mendieta:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def estado(self):
        return "Aprobado" if self.promedio() >= 3.0 else "Reprobado"

if __name__ == "__main__":
    estudiante = felipe_mendieta("Felipe", [4.5, 3.8, 2.9])
    print(estudiante.nombre, estudiante.promedio(), estudiante.estado())
