# Este es el archivo n�mero 95
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def evaluar(self):
        if self.numero > 0: return "Positivo"
        elif self.numero < 0: return "Negativo"
        else: return "Cero"

n = felipe_mendieta(-3)
print("Tipo:", n.evaluar())
