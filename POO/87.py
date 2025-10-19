# Este es el archivo n�mero 87
class felipe_mendieta:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(self):
        if self.nota >= 4.5:
            letra = "A"
        elif self.nota >= 4.0:
            letra = "B"
        elif self.nota >= 3.0:
            letra = "C"
        else:
            letra = "D"
        print(f"{self.nombre}: {letra}")

est = felipe_mendieta("Laura", 4.2)
est.resultado()
