# Este es el archivo n�mero 47
class felipe_mendieta:
    def __init__(self, palabra, letra):
        self.palabra = palabra
        self.letra = letra

    def contiene(self):
        return self.letra.lower() in self.palabra.lower()

p = felipe_mendieta("Python", "y")
print("¿Contiene la letra?", p.contiene())
