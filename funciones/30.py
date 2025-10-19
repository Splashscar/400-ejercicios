# Este es el archivo n�mero 30
class felipe_mendieta:
    def __init__(self):
        self.cuentas = {}

    def crear_cuenta(self, nombre, saldo):
        self.cuentas[nombre] = saldo

    def mostrar_cuentas(self):
        for nombre, saldo in self.cuentas.items():
            print(f"{nombre}: ${saldo}")

banco = felipe_mendieta()
banco.crear_cuenta("Felipe", 1000)
banco.crear_cuenta("Juan", 500)
banco.mostrar_cuentas()
