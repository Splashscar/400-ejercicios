# Este es el archivo n�mero 85
class felipe_mendieta:
    def __init__(self):
        self.libros_prestados = []

    def prestar(self, titulo):
        self.libros_prestados.append(titulo)
        print(f"Libro '{titulo}' prestado.")

    def listar(self):
        print("Libros prestados:", ", ".join(self.libros_prestados))

biblio = felipe_mendieta()
biblio.prestar("Don Quijote")
biblio.prestar("El Principito")
biblio.listar()
