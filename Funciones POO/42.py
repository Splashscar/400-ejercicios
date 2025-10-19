# Este es el archivo n�mero 42
class felipe_mendieta:
    def __init__(self, año):
        self.año = año

    def es_bisiesto(self):
        return (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0)

a = felipe_mendieta(2024)
print("¿Es bisiesto?", a.es_bisiesto())
