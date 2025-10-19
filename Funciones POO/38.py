# Este es el archivo n�mero 38
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def tipo(self):
        if self.numero > 0:
            return "Positivo"
        elif self.numero < 0:
            return "Negativo"
        else:
            return "Cero"

n = felipe_mendieta(-5)
print("El número es:", n.tipo())
