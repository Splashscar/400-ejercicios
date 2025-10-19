# Este es el archivo n�mero 85
class felipe_mendieta:
    def __init__(self, peso):
        self.peso = peso

    def costo_envio(self):
        if self.peso <= 5:
            return 10000
        else:
            return 10000 + (self.peso - 5) * 2000

envio = felipe_mendieta(8)
print("Costo de envío:", envio.costo_envio())
