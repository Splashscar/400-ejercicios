# Este es el archivo n�mero 71
class felipe_mendieta:
    def __init__(self, nombre, deuda):
        self.nombre = nombre
        self.deuda = deuda

    def pagar(self, abono):
        self.deuda -= abono
        print(f"{self.nombre} debe ahora ${self.deuda}")

cliente = felipe_mendieta("Felipe", 500000)
cliente.pagar(200000)
