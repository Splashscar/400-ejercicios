# Este es el archivo n�mero 18
class felipe_mendieta:
    def __init__(self, parcial, final):
        self.parcial = parcial
        self.final = final

    def nota_final(self):
        return (self.parcial * 0.6) + (self.final * 0.4)

nota = felipe_mendieta(4.2, 3.8)
print("Nota final:", nota.nota_final())
