# Este es el archivo n�mero 69
class felipe_mendieta:
    def __init__(self, numero, minimo, maximo):
        self.numero = numero
        self.minimo = minimo
        self.maximo = maximo

    def dentro_rango(self):
        return self.minimo <= self.numero <= self.maximo

r = felipe_mendieta(12, 10, 20)
print("¿Está en rango?", r.dentro_rango())
