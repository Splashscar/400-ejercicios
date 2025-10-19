# Este es el archivo n�mero 31
class felipe_mendieta:
    def __init__(self, mes, anio):
        self.mes = mes
        self.anio = anio

    def mostrar(self):
        return f"Calendario del mes {self.mes} del año {self.anio}"

cal = felipe_mendieta("Octubre", 2025)
print(cal.mostrar())
