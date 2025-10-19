# Este es el archivo n�mero 45
class felipe_mendieta:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, grado):
        self.estudiantes.append({"nombre": nombre, "grado": grado})

    def listar_estudiantes(self):
        for e in self.estudiantes:
            print(f"{e['nombre']} está en grado {e['grado']}")

colegio = felipe_mendieta()
colegio.agregar_estudiante("Felipe", "11°")
colegio.agregar_estudiante("Sofía", "10°")
colegio.listar_estudiantes()
