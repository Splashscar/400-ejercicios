# Este es el archivo n�mero 77
class felipe_mendieta:
    def __init__(self, tarifa):
        self.tarifa = tarifa

    def cobrar(self, horas):
        print("Total a pagar:", horas * self.tarifa)

parking = felipe_mendieta(2500)
parking.cobrar(3)
