# Este es el archivo n�mero 90
import random
import string

class felipe_mendieta:
    def generar(self, longitud):
        caracteres = string.ascii_letters + string.digits + "!@#$%&*"
        return ''.join(random.choice(caracteres) for _ in range(longitud))

gen = felipe_mendieta()
print("Contraseña generada:", gen.generar(10))
