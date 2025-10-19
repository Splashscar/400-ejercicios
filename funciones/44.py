# Este es el archivo n�mero 44
class felipe_mendieta:
    def __init__(self):
        self.pacientes = []

    def registrar_paciente(self, nombre, edad):
        self.pacientes.append({"nombre": nombre, "edad": edad})

    def listar_pacientes(self):
        for p in self.pacientes:
            print(f"{p['nombre']} ({p['edad']} años)")

hospital = felipe_mendieta()
hospital.registrar_paciente("Felipe", 25)
hospital.registrar_paciente("Laura", 30)
hospital.listar_pacientes()
