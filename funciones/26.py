# Este es el archivo n�mero 26
class felipe_mendieta:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hablar(self):
        if self.especie.lower() == "perro":
            return "Guau 🐾"
        elif self.especie.lower() == "gato":
            return "Miau 🐱"
        else:
            return "Sonido desconocido"

mascota = felipe_mendieta("Luna", "Gato")
print(mascota.hablar())
