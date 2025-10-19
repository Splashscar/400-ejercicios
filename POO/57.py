# Este es el archivo n�mero 57
class felipe_mendieta:
    def __init__(self, mensual, meses):
        self.mensual = mensual
        self.meses = meses

    def total(self):
        total = self.mensual * self.meses
        print(f"Ahorro total en {self.meses} meses: ${total}")

ahorro = felipe_mendieta(50000, 12)
ahorro.total()
