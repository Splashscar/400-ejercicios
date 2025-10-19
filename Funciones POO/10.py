# Este es el archivo n�mero 10
class felipe_mendieta:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        f = 1
        for i in range(1, self.n + 1):
            f *= i
        return f

fac = felipe_mendieta(5)
print("Factorial:", fac.factorial())
