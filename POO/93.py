# Este es el archivo n�mero 93
class felipe_mendieta:
    def __init__(self, total, dia):
        self.total = total
        self.dia = dia

    def descuento(self):
        if self.dia == "martes":
            total = self.total * 0.9
        else:
            total = self.total
        print("Total a pagar:", total)

factura = felipe_mendieta(120000, "martes")
factura.descuento()
