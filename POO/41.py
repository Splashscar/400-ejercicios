# Este es el archivo n�mero 41
class felipe_mendieta:
    def __init__(self, nombre, noches, precio_noche):
        self.nombre = nombre
        self.noches = noches
        self.precio_noche = precio_noche

    def total(self):
        total = self.noches * self.precio_noche
        print(f"{self.nombre} pagará ${total}")

cliente = felipe_mendieta("Ana", 3, 150000)
cliente.total()
