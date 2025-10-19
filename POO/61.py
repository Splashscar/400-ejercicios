# Este es el archivo n�mero 61
class felipe_mendieta:
    def __init__(self, total, porcentaje):
        self.total = total
        self.porcentaje = porcentaje

    def propina(self):
        print("Propina:", self.total * self.porcentaje / 100)

cuenta = felipe_mendieta(200000, 10)
cuenta.propina()
