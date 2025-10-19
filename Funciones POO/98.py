# Este es el archivo n�mero 98
class felipe_mendieta:
    def __init__(self, celsius):
        self.celsius = celsius

    def convertir(self):
        return (self.celsius * 9/5) + 32

t = felipe_mendieta(25)
print("Fahrenheit:", t.convertir())
