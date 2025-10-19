# Este es el archivo n�mero 53
class felipe_mendieta:
    def __init__(self):
        self.usuarios = {"admin": "1234", "felipe": "abcd"}

    def iniciar_sesion(self, usuario, clave):
        if usuario in self.usuarios and self.usuarios[usuario] == clave:
            return "Inicio de sesión exitoso ✅"
        return "Usuario o contraseña incorrectos ❌"

login = felipe_mendieta()
print(login.iniciar_sesion("felipe", "abcd"))
