# Este es el archivo n�mero 77
class felipe_mendieta:
    def area_rectangulo(self, base, altura):
        return base * altura

    def area_circulo(self, radio):
        return 3.1416 * (radio ** 2)

calc = felipe_mendieta()
print("Área del rectángulo:", calc.area_rectangulo(5, 3))
print("Área del círculo:", calc.area_circulo(4))
