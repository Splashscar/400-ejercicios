# Este es el archivo n�mero 52
import time
class felipe_mendieta:
    def __init__(self, segundos):
        self.segundos = segundos

    def contar(self):
        for i in range(self.segundos, 0, -1):
            print(i)
            time.sleep(1)
        print("¡Tiempo cumplido!")

reloj = felipe_mendieta(3)
reloj.contar()
