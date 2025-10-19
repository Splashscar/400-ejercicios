# Este es el archivo n�mero 39
class felipe_mendieta:
    def __init__(self):
        self.empleados = []

    def registrar(self, nombre, salario):
        self.empleados.append({"nombre": nombre, "salario": salario})

    def listar(self):
        for emp in self.empleados:
            print(f"{emp['nombre']} gana ${emp['salario']}")

empresa = felipe_mendieta()
empresa.registrar("Felipe", 2500)
empresa.registrar("Laura", 3000)
empresa.listar()
