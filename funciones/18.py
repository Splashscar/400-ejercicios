# Este es el archivo n�mero 18
class felipe_mendieta:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso

    def calcular_costo(self):
        if self.peso <= 5:
            return 10000
        else:
            return 10000 + (self.peso - 5) * 2000

if __name__ == "__main__":
    envio = felipe_mendieta("Bogotá", 8)
    print("Costo del envío:", envio.calcular_costo())
