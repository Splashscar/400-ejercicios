# Este es el archivo n�mero 64
class felipe_mendieta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def listar_jugadores(self):
        print(f"Equipo {self.nombre}: {', '.join(self.jugadores)}")

equipo = felipe_mendieta("Los Vikingos FC")
equipo.agregar_jugador("Eivor")
equipo.agregar_jugador("Basim")
equipo.listar_jugadores()
