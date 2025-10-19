# Este es el archivo n�mero 8
class felipe_mendieta:
    def __init__ (self, calculo):
        self.calculo = calculo
    def factorial(self):
        if self.calculo < 0:
            return "El factorial no está definido para números negativos."
        resultado = 1
        for i in range(1, self.calculo + 1):
            resultado *= i
        return resultado
numero = 5
factorial_calculo = felipe_mendieta(numero)
resultado = factorial_calculo.factorial()
print(f"El factorial de {numero} es: {resultado}")