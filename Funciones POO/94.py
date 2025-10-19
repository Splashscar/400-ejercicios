# Este es el archivo n�mero 94
class felipe_mendieta:
    def __init__(self):
        self.asistencia = []

    def marcar(self, nombre):
        self.asistencia.append(nombre)

    def mostrar(self):
        return self.asistencia

clase = felipe_mendieta()
clase.marcar("Laura")
clase.marcar("Felipe")
print("Asistencia:", clase.mostrar())
