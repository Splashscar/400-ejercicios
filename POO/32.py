# Este es el archivo n�mero 32
import time
class felipe_mendieta:
    def __init__(self, segundos):
        self.segundos = segundos

    def iniciar(self):
        print("Temporizador iniciado...")
        time.sleep(self.segundos)
        print("¡Tiempo terminado!")

timer = felipe_mendieta(2)
timer.iniciar()
