# Este es el archivo n�mero 70
import random

class felipe_mendieta:
    def lanzar(self):
        return random.randint(1, 6)

dado = felipe_mendieta()
print("Resultado del dado:", dado.lanzar())
