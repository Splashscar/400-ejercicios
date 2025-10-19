# Este es el archivo n�mero 19
class felipe_mendieta:
    def __init__(self):
        self.encendido = False

    def prender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def estado(self):
        return "Encendido" if self.encendido else "Apagado"

if __name__ == "__main__":
    luz = felipe_mendieta()
    luz.prender()
    print(luz.estado())
