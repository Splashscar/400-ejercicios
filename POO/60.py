# Este es el archivo n�mero 60
class felipe_mendieta:
    def __init__(self, piso_actual):
        self.piso_actual = piso_actual

    def ir_a(self, destino):
        if destino > self.piso_actual:
            print(f"Subiendo del piso {self.piso_actual} al {destino}")
        elif destino < self.piso_actual:
            print(f"Bajando del piso {self.piso_actual} al {destino}")
        else:
            print("Ya estás en ese piso")

ascensor = felipe_mendieta(3)
ascensor.ir_a(7)
