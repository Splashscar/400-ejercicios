# Este es el archivo n�mero 16
from datetime import datetime

class felipe_mendieta:
    def hora_actual(self):
        return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    reloj = felipe_mendieta()
    print("Hora actual:", reloj.hora_actual())
