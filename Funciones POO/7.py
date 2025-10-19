# Este es el archivo n�mero 7
class felipe_mendieta:
    def __init__(self, precio):
        self.precio = precio

    def con_iva(self):
        return self.precio * 1.19

p = felipe_mendieta(50000)
print("Precio con IVA:", p.con_iva())
