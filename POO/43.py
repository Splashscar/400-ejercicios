# Este es el archivo n�mero 43
class felipe_mendieta:
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def mostrar(self):
        for nombre, telefono in self.contactos.items():
            print(f"{nombre}: {telefono}")

agenda = felipe_mendieta()
agenda.agregar("Luis", "3102457896")
agenda.agregar("Sofía", "3001122334")
agenda.mostrar()
