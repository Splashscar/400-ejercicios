# Este es el archivo n�mero 22
class felipe_mendieta:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        prom = sum(self.notas) / len(self.notas)
        print(f"{self.nombre} tiene un promedio de {prom:.2f}")

est = felipe_mendieta("Laura", [4.5, 3.8, 4.0, 5.0])
est.promedio()
