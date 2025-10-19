# Este es el archivo n�mero 79
class felipe_mendieta:
    def __init__(self):
        self.turnos = []

    def agregar(self, nombre):
        self.turnos.append(nombre)

    def siguiente(self):
        print("Siguiente:", self.turnos.pop(0))

fila = felipe_mendieta()
fila.agregar("Pedro")
fila.agregar("Juan")
fila.siguiente()
