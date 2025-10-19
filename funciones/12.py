# Este es el archivo n�mero 12
class felipe_mendieta:
    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

if __name__ == "__main__":
    calc = felipe_mendieta()
    print(calc.sumar(5, 3))
    print(calc.dividir(10, 0))
