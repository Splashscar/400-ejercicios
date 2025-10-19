# Este es el archivo n�mero 32
class felipe_mendieta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comparar(self):
        if self.a > self.b:
            return f"{self.a} es mayor que {self.b}"
        elif self.a < self.b:
            return f"{self.b} es mayor que {self.a}"
        else:
            return "Ambos son iguales"

comparador = felipe_mendieta(8, 5)
print(comparador.comparar())
