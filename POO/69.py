# Este es el archivo n�mero 69
class felipe_mendieta:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def ingresar(self, u, c):
        if u == self.usuario and c == self.contraseña:
            print("Acceso permitido 🔓")
        else:
            print("Acceso denegado 🔒")

login = felipe_mendieta("admin", "1234")
login.ingresar("admin", "1234")
