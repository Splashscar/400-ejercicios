# Este es el archivo n�mero 82
class felipe_mendieta:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def imc(self):
        return round(self.peso / (self.altura ** 2), 2)

persona = felipe_mendieta(70, 1.75)
print("IMC:", persona.imc())
