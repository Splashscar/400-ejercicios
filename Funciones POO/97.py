# Este es el archivo n�mero 97
class felipe_mendieta:
    def __init__(self, horas, pago_hora):
        self.horas = horas
        self.pago_hora = pago_hora

    def salario(self):
        if self.horas > 40:
            extras = (self.horas - 40) * (self.pago_hora * 1.5)
            return (40 * self.pago_hora) + extras
        return self.horas * self.pago_hora

trabajador = felipe_mendieta(45, 10000)
print("Salario semanal:", trabajador.salario())
