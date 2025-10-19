# Este es el archivo n�mero 9
class felipe_mendieta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mayor(self):
        return max(self.a, self.b)

num = felipe_mendieta(15, 23)
print("El mayor es:", num.mayor())
