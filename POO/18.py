# Este es el archivo n�mero 18
class felipe_mendieta:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        print(f"Vehículo: {self.marca}, Modelo: {self.modelo}")

carro = felipe_mendieta("Toyota", "Corolla 2022")
carro.info()
