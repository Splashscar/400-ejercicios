# Este es el archivo n�mero 91
class felipe_mendieta:
    def sumar(self, a, b): return a + b
    def restar(self, a, b): return a - b
    def multiplicar(self, a, b): return a * b
    def dividir(self, a, b): return a / b if b != 0 else "Error: división por cero"

calc = felipe_mendieta()
print("Suma:", calc.sumar(4, 5))
