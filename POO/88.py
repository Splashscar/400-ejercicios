# Este es el archivo n�mero 88
class felipe_mendieta:
    def __init__(self, horas, tarifa):
        self.horas = horas
        self.tarifa = tarifa

    def salario(self):
        if self.horas > 40:
            extra = (self.horas - 40) * (self.tarifa * 1.5)
            total = (40 * self.tarifa) + extra
        else:
            total = self.horas * self.tarifa
        print("Salario semanal:", total)

trabajador = felipe_mendieta(45, 10000)
trabajador.salario()
