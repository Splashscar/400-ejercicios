# Este es el archivo n�mero 61
class felipe_mendieta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.config = {"tema": "claro", "notificaciones": True}

    def cambiar_tema(self, nuevo_tema):
        self.config["tema"] = nuevo_tema

    def mostrar_config(self):
        return f"Usuario: {self.nombre}, Configuración: {self.config}"

user = felipe_mendieta("Felipe")
user.cambiar_tema("oscuro")
print(user.mostrar_config())
