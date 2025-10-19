# Este es el archivo n�mero 66
class felipe_mendieta:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio**2

c = felipe_mendieta(4)
print("Área del círculo:", round(c.area(), 2))
