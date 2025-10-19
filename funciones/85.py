# Este es el archivo n�mero 85
class felipe_mendieta:
    def calcular(self, cuenta, porcentaje):
        propina = cuenta * (porcentaje / 100)
        total = cuenta + propina
        return f"Propina: ${propina}, Total a pagar: ${total}"

calc = felipe_mendieta()
print(calc.calcular(50000, 10))
