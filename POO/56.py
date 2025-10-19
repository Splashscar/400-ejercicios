# Este es el archivo n�mero 56
class felipe_mendieta:
    def __init__(self):
        self.notas = {}

    def agregar(self, nombre, nota):
        self.notas[nombre] = nota

    def mostrar(self):
        for n, nota in self.notas.items():
            print(f"{n}: {nota}")

notas = felipe_mendieta()
notas.agregar("Ana", 4.7)
notas.agregar("Luis", 3.9)
notas.mostrar()
