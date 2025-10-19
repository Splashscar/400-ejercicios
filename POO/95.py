# Este es el archivo n�mero 95
class felipe_mendieta:
    def __init__(self):
        self.peliculas = {}

    def agregar(self, titulo, rating):
        self.peliculas[titulo] = rating

    def mostrar(self):
        for t, r in self.peliculas.items():
            print(f"{t}: {r}/5 estrellas")

cine = felipe_mendieta()
cine.agregar("Avatar", 5)
cine.agregar("Titanic", 4)
cine.mostrar()
