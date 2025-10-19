# Este es el archivo n�mero 50
class felipe_mendieta:
    def __init__(self):
        self.paises = {"Colombia": 20000, "México": 35000, "EEUU": 50000}

    def calcular_envio(self, destino, peso):
        if destino not in self.paises:
            return "Destino no disponible."
        costo = self.paises[destino] + (peso * 2000)
        return f"Costo total del envío a {destino}: ${costo}"

envio = felipe_mendieta()
print(envio.calcular_envio("México", 3))
