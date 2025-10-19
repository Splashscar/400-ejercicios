# Este es el archivo n�mero 46
class felipe_mendieta:
    def __init__(self):
        self.asistencia = {}

    def registrar(self, nombre, presente):
        self.asistencia[nombre] = presente

    def mostrar(self):
        for n, p in self.asistencia.items():
            estado = "Presente" if p else "Ausente"
            print(f"{n}: {estado}")

control = felipe_mendieta()
control.registrar("Daniel", True)
control.registrar("María", False)
control.mostrar()
