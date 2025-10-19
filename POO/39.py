# Este es el archivo n�mero 39
class felipe_mendieta:
    def __init__(self):
        self.libros = []

    def agregar(self, titulo):
        self.libros.append(titulo)

    def mostrar(self):
        print("Libros disponibles:")
        for libro in self.libros:
            print("-", libro)

bib = felipe_mendieta()
bib.agregar("Cien años de soledad")
bib.agregar("El Principito")
bib.mostrar()
