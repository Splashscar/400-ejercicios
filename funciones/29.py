# Este es el archivo n�mero 29
class felipe_mendieta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def ganar_puntos(self, puntos):
        self.puntaje += puntos

    def mostrar_puntaje(self):
        return f"{self.nombre} tiene {self.puntaje} puntos"

jugador = felipe_mendieta("Felipe")
jugador.ganar_puntos(50)
print(jugador.mostrar_puntaje())
