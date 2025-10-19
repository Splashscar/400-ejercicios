# Este es el archivo n�mero 58
class felipe_mendieta:
    def __init__(self):
        self.mascotas = []

    def registrar(self, nombre):
        self.mascotas.append(nombre)

    def mostrar(self):
        print("Mascotas registradas:", ", ".join(self.mascotas))

pet = felipe_mendieta()
pet.registrar("Luna")
pet.registrar("Rex")
pet.mostrar()
