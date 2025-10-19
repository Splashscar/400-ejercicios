# Este es el archivo n�mero 5
class felipe_mendieta:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def promedio(self):
        return (self.n1 + self.n2 + self.n3) / 3

est = felipe_mendieta(4.0, 3.5, 4.8)
print("Promedio:", est.promedio())
