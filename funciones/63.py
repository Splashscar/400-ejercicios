# Este es el archivo n�mero 63
class felipe_mendieta:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor):
        self.libros.append({"titulo": titulo, "autor": autor})

    def listar(self):
        for l in self.libros:
            print(f"📖 {l['titulo']} — {l['autor']}")

biblio = felipe_mendieta()
biblio.agregar_libro("1984", "George Orwell")
biblio.agregar_libro("Assassin’s Creed: Valhalla", "Matthew Stover")
biblio.listar()
