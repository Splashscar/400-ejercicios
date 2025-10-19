# Este es el archivo n�mero 15
class felipe_mendieta:
    def __init__(self, usuario, correo):
        self.usuario = usuario
        self.correo = correo

    def mostrar(self):
        print(f"Usuario: {self.usuario}, Correo: {self.correo}")

user = felipe_mendieta("felipe", "felipe@mail.com")
user.mostrar()
