# Este es el archivo n�mero 37
class felipe_mendieta:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return "Sin notas registradas"
        return sum(self.notas) / len(self.notas)

notas = felipe_mendieta()
notas.agregar_nota(4.0)
notas.agregar_nota(3.5)
print("Promedio:", notas.promedio())
