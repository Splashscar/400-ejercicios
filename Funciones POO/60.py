# Este es el archivo n�mero 60
class felipe_mendieta:
    def __init__(self, n1, n2, n3):
        self.n1, self.n2, self.n3 = n1, n2, n3

    def promedio(self):
        return (self.n1 + self.n2 + self.n3) / 3

notas = felipe_mendieta(3.5, 4.0, 5.0)
print("Promedio:", round(notas.promedio(), 2))
