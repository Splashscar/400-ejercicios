# Este es el archivo n�mero 2
class felipe_mendieta:
    def __init__(self, saldo, tasa_interes):
        self.saldo = saldo
        self.tasa_interes = tasa_interes
    def calcular_interes(self, años):
        interes = self.saldo * (self.tasa_interes / 100) * años
        return interes
    
cuenta = felipe_mendieta(1000, 5)
interes_ganado = cuenta.calcular_interes(3)
print(f"Interés ganado en 3 años: {interes_ganado}")