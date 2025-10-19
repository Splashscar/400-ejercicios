# Este es el archivo n�mero 17
class felipe_mendieta:
    def __init__(self, clave):
        self.clave = clave

    def es_segura(self):
        return len(self.clave) >= 8 and any(c.isdigit() for c in self.clave)

user = felipe_mendieta("clave123")
print("¿Contraseña segura?", user.es_segura())
