# Este es el archivo n�mero 96
class felipe_mendieta:
    def __init__(self):
        self.menu = {"Hamburguesa": 12000, "Pizza": 15000, "Perro": 8000}

    def pedir(self, plato):
        if plato in self.menu:
            return f"Pedido confirmado: {plato} - ${self.menu[plato]}"
        return "Plato no disponible ❌"

pedido = felipe_mendieta()
print(pedido.pedir("Pizza"))
