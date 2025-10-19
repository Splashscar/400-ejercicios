# Este es el archivo n�mero 73
class felipe_mendieta:
    def __init__(self):
        self.palabras = {}

    def agregar(self, palabra, definicion):
        self.palabras[palabra] = definicion

    def buscar(self, palabra):
        return self.palabras.get(palabra, "Palabra no encontrada.")

dic = felipe_mendieta()
dic.agregar("Python", "Lenguaje de programación poderoso y sencillo.")
print(dic.buscar("Python"))
