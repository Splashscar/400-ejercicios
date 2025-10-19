# Este es el archivo n�mero 86
class felipe_mendieta:
    def __init__(self, ventas, porcentaje):
        self.ventas = ventas
        self.porcentaje = porcentaje

    def comision(self):
        print("Comisión:", self.ventas * self.porcentaje / 100)

vendedor = felipe_mendieta(800000, 5)
vendedor.comision()
