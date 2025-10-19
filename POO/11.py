# Este es el archivo n�mero 11
class felipe_mendieta:
    def __init__(self, km):
        self.km = km

    def a_millas(self):
        print(f"{self.km} km = {self.km * 0.621371:.2f} millas")

dist = felipe_mendieta(10)
dist.a_millas()
