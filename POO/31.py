# Este es el archivo n�mero 31
class felipe_mendieta:
    def __init__(self):
        self.asistencia = []

    def registrar(self, nombre):
        self.asistencia.append(nombre)

    def mostrar(self):
        print("Asistentes:")
        for n in self.asistencia:
            print("-", n)

clase = felipe_mendieta()
clase.registrar("Ana")
clase.registrar("Luis")
clase.mostrar()
