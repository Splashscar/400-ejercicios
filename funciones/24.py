# Este es el archivo n�mero 24
class felipe_mendieta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.altura = 0

    def despegar(self):
        self.altura = 1000
        return f"{self.nombre} ha despegado y está a {self.altura} metros."

    def aterrizar(self):
        self.altura = 0
        return f"{self.nombre} ha aterrizado con éxito."

cohete = felipe_mendieta("Apolo X")
print(cohete.despegar())
print(cohete.aterrizar())
