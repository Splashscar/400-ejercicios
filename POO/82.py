# Este es el archivo n�mero 82
class felipe_mendieta:
    def __init__(self):
        self.tickets = []

    def crear_ticket(self, asunto):
        self.tickets.append(asunto)

    def listar(self):
        for i, t in enumerate(self.tickets, 1):
            print(f"#{i} - {t}")

soporte = felipe_mendieta()
soporte.crear_ticket("Error en el login")
soporte.crear_ticket("Problema de red")
soporte.listar()
