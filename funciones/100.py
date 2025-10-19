# Este es el archivo n�mero 100
class felipe_mendieta:
    def __init__(self):
        self.asistentes = []

    def registrar(self, nombre):
        self.asistentes.append(nombre)

    def mostrar(self):
        print("Asistentes registrados:")
        for a in self.asistentes:
            print("-", a)

clase = felipe_mendieta()
clase.registrar("Felipe")
clase.registrar("Miguel")
clase.mostrar()
