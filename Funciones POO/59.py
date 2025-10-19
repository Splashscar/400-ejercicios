# Este es el archivo n�mero 59
class felipe_mendieta:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        resultado = 1
        for i in range(1, self.n + 1):
            resultado *= i
        return resultado

num = felipe_mendieta(5)
print("Factorial:", num.factorial())
