# Este es el archivo n�mero 70
class felipe_mendieta:
    def __init__(self, año):
        self.año = año

    def verificar(self):
        if (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0):
            print("Año bisiesto ✅")
        else:
            print("Año normal")

anio = felipe_mendieta(2024)
anio.verificar()
