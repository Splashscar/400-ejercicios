# Este es el archivo n�mero 94
class felipe_mendieta:
    def calcular(self, kwh):
        tarifa = 620.50
        total = kwh * tarifa
        return f"Total a pagar por {kwh} kWh es ${total}"

medidor = felipe_mendieta()
print(medidor.calcular(130))
