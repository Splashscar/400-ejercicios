# Este es el archivo n�mero 6
class felipe_mendieta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def operaciones(self):
        print("Suma:", self.x + self.y)
        print("Resta:", self.x - self.y)
        print("Multiplicación:", self.x * self.y)
        print("División:", self.x / self.y)

calc = felipe_mendieta(12, 3)
calc.operaciones()
