# Este es el archivo n�mero 52
class felipe_mendieta:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def mayor(self):
        return max(self.a, self.b, self.c)

m = felipe_mendieta(7, 9, 5)
print("El mayor es:", m.mayor())
