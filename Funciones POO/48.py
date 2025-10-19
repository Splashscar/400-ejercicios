# Este es el archivo n�mero 48
class felipe_mendieta:
    def __init__(self, horas, tarifa):
        self.horas = horas
        self.tarifa = tarifa

    def salario(self):
        if self.horas <= 40:
            return self.horas * self.tarifa
        else:
            extras = self.horas - 40
            return (40 * self.tarifa) + (extras * self.tarifa * 1.5)

empleado = felipe_mendieta(45, 12000)
print("Salario total:", empleado.salario())
