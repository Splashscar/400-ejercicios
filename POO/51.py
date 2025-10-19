# Este es el archivo n�mero 51
class felipe_mendieta:
    def __init__(self):
        self.empleados = {}

    def agregar(self, nombre, cargo):
        self.empleados[nombre] = cargo

    def mostrar(self):
        for n, c in self.empleados.items():
            print(f"{n} - {c}")

empresa = felipe_mendieta()
empresa.agregar("Carlos", "Gerente")
empresa.agregar("Marta", "Contadora")
empresa.mostrar()
