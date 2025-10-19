# Este es el archivo n�mero 99
class felipe_mendieta:
    def calcular(self, peso, altura):
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return f"IMC: {imc:.2f} - Bajo peso"
        elif imc < 25:
            return f"IMC: {imc:.2f} - Normal"
        elif imc < 30:
            return f"IMC: {imc:.2f} - Sobrepeso"
        else:
            return f"IMC: {imc:.2f} - Obesidad"

calc = felipe_mendieta()
print(calc.calcular(61, 1.71))
