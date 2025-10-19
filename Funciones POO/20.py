# Este es el archivo n�mero 20
class felipe_mendieta:
    def __init__(self, km):
        self.km = km

    def millas(self):
        return self.km * 0.621371

dist = felipe_mendieta(10)
print("Millas:", dist.millas())
