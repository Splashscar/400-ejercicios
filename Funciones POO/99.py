# Este es el archivo n�mero 99
import random, string

class felipe_mendieta:
    def generar(self, longitud):
        caracteres = string.ascii_letters + string.digits
        return "".join(random.choice(caracteres) for _ in range(longitud))

g = felipe_mendieta()
print("Contraseña:", g.generar(10))
