# Este es el archivo n�mero 50
class felipe_mendieta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        print("Suma:", self.a + self.b)

    def restar(self):
        print("Resta:", self.a - self.b)

calc = felipe_mendieta(10, 5)
calc.sumar()
calc.restar()
