# Este es el archivo n�mero 75
class felipe_mendieta:
    def __init__(self):
        self.cuentas = {}

    def guardar(self, sitio, clave):
        self.cuentas[sitio] = clave

    def mostrar(self):
        for sitio, clave in self.cuentas.items():
            print(f"{sitio}: {clave}")

gestor = felipe_mendieta()
gestor.guardar("Instagram", "clave123")
gestor.guardar("Gmail", "pass2025")
gestor.mostrar()
