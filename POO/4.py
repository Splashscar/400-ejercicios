# Este es el archivo n�mero 4
class felipe_mendieta:
    def __init__(self, celsius):
        self.celsius = celsius

    def a_fahrenheit(self):
        f = (self.celsius * 9/5) + 32
        print(f"{self.celsius}°C = {f}°F")

temp = felipe_mendieta(25)
temp.a_fahrenheit()
