# Este es el archivo n�mero 35
class felipe_mendieta:
    def __init__(self):
        self.frutas = []

    def agregar(self, fruta):
        self.frutas.append(fruta)

    def mostrar(self):
        return f"Frutas: {', '.join(self.frutas)}"

lista = felipe_mendieta()
lista.agregar("Manzana")
lista.agregar("Pera")
print(lista.mostrar())
