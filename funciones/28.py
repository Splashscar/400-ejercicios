# Este es el archivo n�mero 28
class felipe_mendieta:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def mayor(self):
        return max(self.datos)

    def menor(self):
        return min(self.datos)

estad = felipe_mendieta([3, 7, 5, 10])
print("Promedio:", estad.promedio())
print("Mayor:", estad.mayor())
