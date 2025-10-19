# Este es el archivo n�mero 99
class felipe_mendieta:
    def __init__(self):
        self.temperaturas = []

    def registrar(self, valor):
        self.temperaturas.append(valor)

    def promedio(self):
        print("Promedio:", sum(self.temperaturas) / len(self.temperaturas))

temp = felipe_mendieta()
temp.registrar(20)
temp.registrar(25)
temp.registrar(23)
temp.promedio()
