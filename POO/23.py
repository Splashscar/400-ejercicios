# Este es el archivo n�mero 23
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero

    def es_primo(self):
        if self.numero < 2:
            print("No es primo")
            return
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                print("No es primo")
                return
        print("Es primo")

num = felipe_mendieta(7)
num.es_primo()
