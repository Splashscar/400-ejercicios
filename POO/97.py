# Este es el archivo n�mero 97
class felipe_mendieta:
    def __init__(self):
        self.eventos = []

    def agregar(self, evento):
        self.eventos.append(evento)

    def mostrar(self):
        for e in self.eventos:
            print("-", e)

agenda = felipe_mendieta()
agenda.agregar("Reunión ADSO")
agenda.agregar("Entrega proyecto")
agenda.mostrar()
