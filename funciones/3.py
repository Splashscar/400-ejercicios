# Este es el archivo n�mero 3
class felipe_mendieta:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area
triangulo = felipe_mendieta(5, 10)
area_triangulo = triangulo.calcular_area()
print(f"El área del triángulo es: {area_triangulo}")