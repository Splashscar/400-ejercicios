# Este es el archivo n�mero 6
class felipe_mendieta:
    def __init__(self, edad):
        self.edad = edad

    def es_mayor(self):
        return self.edad >= 18

p = felipe_mendieta(20)
print("¿Mayor de edad?", p.es_mayor())
