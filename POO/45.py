# Este es el archivo n�mero 45
class felipe_mendieta:
    def __init__(self):
        self.votos = {"A": 0, "B": 0}

    def votar(self, candidato):
        if candidato in self.votos:
            self.votos[candidato] += 1

    def resultados(self):
        print("Resultados:", self.votos)

votacion = felipe_mendieta()
votacion.votar("A")
votacion.votar("B")
votacion.votar("A")
votacion.resultados()
