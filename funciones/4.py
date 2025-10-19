# Este es el archivo n�mero 4
class felipe_mendieta:
    def __init__(self, numero):
        self.numero = numero
    def es_primo(self):
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero**0.5) + 1):
            if self.numero % i == 0:
                return False
        return True
numero = 29
prueba = felipe_mendieta(numero)
if prueba.es_primo():
    print(f"El número {numero} es primo.")