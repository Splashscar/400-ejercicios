# Este es el archivo n�mero 81
class felipe_mendieta:
    def __init__(self, carga):
        self.carga = carga

    def usar(self, minutos):
        self.carga -= minutos * 0.5
        if self.carga < 0:
            self.carga = 0
        print("Batería restante:", self.carga, "%")

celular = felipe_mendieta(100)
celular.usar(30)
