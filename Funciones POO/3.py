# Este es el archivo n�mero 3
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def es_par(self):
        return self.numero % 2 == 0

num = felipe_mendieta(8)
print("¿Es par?", num.es_par())
