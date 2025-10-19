# Este es el archivo n�mero 27
class felipe_mendieta:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"Tu IMC es {imc:.2f}")

persona = felipe_mendieta(70, 1.75)
persona.calcular_imc()
