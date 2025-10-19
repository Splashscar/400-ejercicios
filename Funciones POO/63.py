# Este es el archivo n�mero 63
class felipe_mendieta:
    def __init__(self, total, tipo):
        self.total = total
        self.tipo = tipo.lower()

    def total_final(self):
        if self.tipo == "oro":
            return self.total * 0.8
        elif self.tipo == "plata":
            return self.total * 0.9
        else:
            return self.total

cliente = felipe_mendieta(100000, "oro")
print("Total con descuento:", cliente.total_final())
