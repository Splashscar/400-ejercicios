# Este es el archivo n�mero 66
class felipe_mendieta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.entrenamientos = []

    def registrar_entrenamiento(self, ejercicio, calorias):
        self.entrenamientos.append({"ejercicio": ejercicio, "calorias": calorias})

    def total_calorias(self):
        return sum(e["calorias"] for e in self.entrenamientos)

gym = felipe_mendieta("Felipe")
gym.registrar_entrenamiento("Correr", 300)
gym.registrar_entrenamiento("Pesas", 200)
print("Total calorías quemadas:", gym.total_calorias())
