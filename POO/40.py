# Este es el archivo n�mero 40
class felipe_mendieta:
    def __init__(self, inicio):
        self.inicio = inicio

    def contar(self):
        for i in range(self.inicio, 0, -1):
            print(i)
        print("¡Despegue!")

c = felipe_mendieta(5)
c.contar()
