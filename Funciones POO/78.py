# Este es el archivo n�mero 78
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def es_primo(self):
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return False
        return True

n = felipe_mendieta(13)
print("¿Es primo?", n.es_primo())
