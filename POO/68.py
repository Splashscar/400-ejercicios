# Este es el archivo n�mero 68
class felipe_mendieta:
    def __init__(self, km, consumo):
        self.km = km
        self.consumo = consumo

    def total(self):
        print("Combustible usado:", self.km / self.consumo, "litros")

viaje = felipe_mendieta(240, 12)
viaje.total()
