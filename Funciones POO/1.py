# Este es el archivo n�mero 1
class felipe_mendieta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

calc = felipe_mendieta(4, 6)
print("Resultado:", calc.sumar())
