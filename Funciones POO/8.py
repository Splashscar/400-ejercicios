# Este es el archivo n�mero 8
class felipe_mendieta:
    def __init__(self, celsius):
        self.celsius = celsius

    def convertir(self):
        return (self.celsius * 9/5) + 32

temp = felipe_mendieta(25)
print("En Fahrenheit:", temp.convertir())
