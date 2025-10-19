# Este es el archivo n�mero 10
class felipe_mendieta:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        res = 1
        for i in range(1, self.n + 1):
            res *= i
        print("Factorial:", res)

num = felipe_mendieta(6)
num.factorial()
