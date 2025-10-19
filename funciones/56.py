# Este es el archivo n�mero 56
class felipe_mendieta:
    def __init__(self):
        self.usuarios = []

    def registrar(self, nombre, correo):
        self.usuarios.append({"nombre": nombre, "correo": correo})

    def mostrar(self):
        for u in self.usuarios:
            print(f"{u['nombre']} - {u['correo']}")

registro = felipe_mendieta()
registro.registrar("Felipe", "felipe@gmail.com")
registro.registrar("Laura", "laura@gmail.com")
registro.mostrar()
