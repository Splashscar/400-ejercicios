# Este es el archivo n�mero 92
class felipe_mendieta:
    def __init__(self):
        self.tareas = []

    def agregar(self, tarea):
        self.tareas.append(tarea)

    def listar(self):
        for i, t in enumerate(self.tareas, 1):
            print(f"{i}. {t}")

todo = felipe_mendieta()
todo.agregar("Estudiar Python")
todo.agregar("Hacer ejercicio")
todo.listar()
