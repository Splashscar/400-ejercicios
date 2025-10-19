# Este es el archivo n�mero 84
class felipe_mendieta:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def login(self, user, pwd):
        return user == self.usuario and pwd == self.contraseña

cuenta = felipe_mendieta("Felipe", "1234")
print("Acceso:", cuenta.login("Felipe", "1234"))
