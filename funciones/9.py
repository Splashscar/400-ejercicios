# Este es el archivo n�mero 9
class felipe_mendieta:
    def __init__ (self, cancion):
        self.cancion = cancion
    def repetir_cancion(self, veces):
        for i in range(veces):
            print(f"{i + 1}: {self.cancion}")
cancion_favorita = "Imagine - John Lennon"
repetidor = felipe_mendieta(cancion_favorita)
repetidor.repetir_cancion(3)