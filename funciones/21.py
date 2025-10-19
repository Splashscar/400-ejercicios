# Este es el archivo n�mero 21
class felipe_mendieta:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def frenar(self, cantidad):
        self.velocidad = max(0, self.velocidad - cantidad)

if __name__ == "__main__":
    carro = felipe_mendieta("Toyota")
    carro.acelerar(60)
    print(f"{carro.marca} va a {carro.velocidad} km/h")
