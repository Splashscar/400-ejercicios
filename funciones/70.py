# Este es el archivo n�mero 70
class felipe_mendieta:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, fecha, descripcion):
        self.eventos.append({"fecha": fecha, "descripcion": descripcion})

    def mostrar_agenda(self):
        for e in self.eventos:
            print(f"{e['fecha']}: {e['descripcion']}")

agenda = felipe_mendieta()
agenda.agregar_evento("2025-10-20", "Ir al gym 🏋️")
agenda.agregar_evento("2025-10-22", "Examen de programación 💻")
agenda.mostrar_agenda()
