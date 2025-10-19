# Este es el archivo n�mero 86
import time

class felipe_mendieta:
    def iniciar(self, segundos):
        for i in range(segundos, 0, -1):
            print(i)
            time.sleep(1)
        print("⏰ ¡Tiempo terminado!")

cronometro = felipe_mendieta()
# cronometro.iniciar(5)
