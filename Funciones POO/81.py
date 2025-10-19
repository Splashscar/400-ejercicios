# Este es el archivo n�mero 81
class felipe_mendieta:
    def __init__(self, celsius):
        self.celsius = celsius

    def a_fahrenheit(self):
        return (self.celsius * 9/5) + 32

t = felipe_mendieta(25)
print("Temperatura en °F:", t.a_fahrenheit())
