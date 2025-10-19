# Este es el archivo n�mero 57
class felipe_mendieta:
    def __init__(self, n):
        self.n = n

    def suma(self):
        return sum(range(1, self.n + 1))

s = felipe_mendieta(10)
print("Suma:", s.suma())
