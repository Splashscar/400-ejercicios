# Este es el archivo n�mero 48
class felipe_mendieta:
    def __init__(self):
        self.libros = []

    def agregar(self, titulo):
        self.libros.append(titulo)

    def mostrar(self):
        print("Libros leídos:")
        for libro in self.libros:
            print("-", libro)

lector = felipe_mendieta()
lector.agregar("1984")
lector.agregar("Crónica de una muerte anunciada")
lector.mostrar()
