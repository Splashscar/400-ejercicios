# Este es el archivo n�mero 20
class felipe_mendieta:
    def celsius_a_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_a_celsius(self, f):
        return (f - 32) * 5/9

if __name__ == "__main__":
    conv = felipe_mendieta()
    print(conv.celsius_a_fahrenheit(25))
