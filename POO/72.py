# Este es el archivo n�mero 72
class felipe_mendieta:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def imc(self):
        valor = self.peso / (self.altura ** 2)
        print("IMC:", round(valor, 2))

persona = felipe_mendieta(70, 1.75)
persona.imc()
