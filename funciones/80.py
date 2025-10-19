# Este es el archivo n�mero 80
class felipe_mendieta:
    def __init__(self, tarifa_hora):
        self.tarifa_hora = tarifa_hora

    def calcular_pago(self, horas):
        return f"Total a pagar: ${horas * self.tarifa_hora}"

parqueadero = felipe_mendieta(3000)
print(parqueadero.calcular_pago(5))
