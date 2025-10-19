# Este es el archivo n�mero 47
class felipe_mendieta:
    def __init__(self, tarifa_base=5000, costo_km=1200):
        self.tarifa_base = tarifa_base
        self.costo_km = costo_km

    def calcular_viaje(self, km):
        total = self.tarifa_base + (km * self.costo_km)
        return f"Costo total del viaje: ${total}"

taxi = felipe_mendieta()
print(taxi.calcular_viaje(8))
