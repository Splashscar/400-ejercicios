# Este es el archivo n�mero 38
import time

class felipe_mendieta:
    def __init__(self, segundos):
        self.segundos = segundos

    def iniciar(self):
        print(f"Iniciando temporizador de {self.segundos} segundos...")
        time.sleep(1)
        print("¡Tiempo terminado! ⏳")

temporizador = felipe_mendieta(1)
temporizador.iniciar()
