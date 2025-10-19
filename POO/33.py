# Este es el archivo n�mero 33
class felipe_mendieta:
    def __init__(self, password):
        self.password = password

    def validar(self):
        if len(self.password) >= 8:
            print("Contraseña segura")
        else:
            print("Contraseña demasiado corta")

clave = felipe_mendieta("python123")
clave.validar()
